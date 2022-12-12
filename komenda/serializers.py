from rest_framework import serializers
from .models import Obywatel, Pracownik, Oddzial, Sprawa, StronyWSprawie, Samochod, Szkoda
from django.contrib.auth.models import User


class ObywatelSerializer(serializers.HyperlinkedModelSerializer):
    imie = serializers.CharField(max_length=22)
    nazwisko = serializers.CharField(max_length=45)
    PESEL = serializers.CharField(max_length=11)
    adres = serializers.CharField(max_length=50)
    telefon = serializers.CharField(max_length=9)

    def validate_imie(self, value):
        if any(char.isdigit() for char in str(value)):
            raise serializers.ValidationError("Imię nie może zawierać cyfr.")
        return value.capitalize()

    def validate_nazwisko(self, value):
        if any(char.isdigit() for char in str(value)):
            raise serializers.ValidationError("Nazwisko nie może zawierać cyfr.")
        return value.capitalize()

    def validate_PESEL(self, value):
        def correct_pesel(pesel) -> bool: # https://www.infor.pl/prawo/gmina/dowod-osobisty/262184,Jak-sprawdzic-czy-masz-poprawny-PESEL.html
            if len(str(pesel)) != 11:
                return False
            multiply = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            dig_sum, i = 0, 0
            for i, digit in enumerate(str(pesel)[:-1]):
                dig_sum += int(digit) * multiply[i]
            dig_sum = 10 - int(str(dig_sum)[-1])
            if dig_sum == int(str(pesel)[-1]):
                return True
            return False

        if not correct_pesel(value):
            raise serializers.ValidationError("Należy podać poprawny PESEL")
        return value

    def validate_telefon(self, value):
        if any(not char.isdigit() for char in str(value)):
            raise serializers.ValidationError("Telefon musi się składać tylko z cyfr")
        if len(value) != 9:
            raise serializers.ValidationError("Numer telefonu musi mieć 9 cyfr")
        return value

    class Meta:
        model = Obywatel
        fields = ['id', 'url', 'imie', 'nazwisko', 'PESEL', 'adres', 'telefon']


class PracownikSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pracownik
        fields = ['url', 'imie', 'nazwisko', 'PESEL', 'adres', 'telefon', 'zarobki', 'id_oddzialu']




class OddzialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Oddzial
        fields = ['url', 'nazwa', 'kierownik']


class SprawaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sprawa
        fields = ['url', 'id_oddzialu', 'opis', 'prowadzacy', 'strona', 'data_zgloszenia', 'w_toku', 'data_zamkniecia']


class StronyWSprawieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StronyWSprawie
        fields = ['url', 'RODZAJ', 'sprawa', 'osoba', 'rodzaj']


class SamochodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Samochod
        fields = ['url', 'nr_rejestracyjny', 'marka', 'model', 'rok_prod', 'silnik', 'ubezpieczenie']


class SzkodaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Szkoda
        fields = ['url', 'opis', 'odszkodowanie', 'samochod']
