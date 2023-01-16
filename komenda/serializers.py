from rest_framework import serializers
from .models import Obywatel, Pracownik, Oddzial, Sprawa, StronyWSprawie, Samochod, Szkoda
from django.contrib.auth.models import User
import datetime


class ObywatelSerializer(serializers.HyperlinkedModelSerializer):
    imie = serializers.CharField(max_length=22)
    nazwisko = serializers.CharField(max_length=45)
    PESEL = serializers.CharField(max_length=11)
    adres = serializers.CharField(max_length=50)
    telefon = serializers.CharField(max_length=9)
    strony_w_sprawie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='stronywsprawie-detail')

    def validate_imie(self, value):
        if any(char.isdigit() for char in str(value)):
            raise serializers.ValidationError("Imię nie może zawierać cyfr.")
        return value.capitalize()

    def validate_nazwisko(self, value):
        if any(char.isdigit() for char in str(value)):
            raise serializers.ValidationError("Nazwisko nie może zawierać cyfr.")
        return value.capitalize()

    def validate_PESEL(self, value):
        def correct_pesel(
                pesel) -> bool:  # https://www.infor.pl/prawo/gmina/dowod-osobisty/262184,Jak-sprawdzic-czy-masz-poprawny-PESEL.html
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
        fields = ['id', 'url', 'imie', 'nazwisko', 'PESEL', 'adres', 'telefon', 'strony_w_sprawie']


class PracownikSerializer(serializers.HyperlinkedModelSerializer):
    imie = serializers.CharField(max_length=22)
    nazwisko = serializers.CharField(max_length=45)
    PESEL = serializers.CharField(max_length=11)
    adres = serializers.CharField(max_length=50)
    telefon = serializers.CharField(max_length=9)
    zarobki = serializers.FloatField(min_value=0)
    # id_oddzialu = serializers.IntegerField(min_value=0)
    id_oddzialu = serializers.SlugRelatedField(queryset=Oddzial.objects.all(), slug_field='nazwa', required=False)
    sprawa = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sprawa-detail')

    def validate_imie(self, value):
        if any(char.isdigit() for char in str(value)):
            raise serializers.ValidationError("Imię nie może zawierać cyfr.")
        return value.capitalize()

    def validate_nazwisko(self, value):
        if any(char.isdigit() for char in str(value)):
            raise serializers.ValidationError("Nazwisko nie może zawierać cyfr.")
        return value.capitalize()

    def validate_PESEL(self, value):
        def correct_pesel(
                pesel) -> bool:  # https://www.infor.pl/prawo/gmina/dowod-osobisty/262184,Jak-sprawdzic-czy-masz-poprawny-PESEL.html
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
        model = Pracownik
        fields = ['url', 'imie', 'nazwisko', 'PESEL', 'adres', 'telefon', 'zarobki', 'id_oddzialu', 'sprawa']


class OddzialSerializer(serializers.HyperlinkedModelSerializer):
    nazwa = serializers.CharField(max_length=45)
    kierownik = serializers.SlugRelatedField(queryset=Pracownik.objects.all(), slug_field='nazwisko')
    pracownik = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='pracownik-detail')
    sprawa = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='sprawa-detail')

    class Meta:
        model = Oddzial
        fields = ['url', 'nazwa', 'kierownik', 'pracownik', 'sprawa']


class SprawaSerializer(serializers.HyperlinkedModelSerializer):
    # id_oddzialu = serializers.IntegerField(min_value=0)
    # prowadzacy = serializers.IntegerField(min_value=0)
    data_zgloszenia = serializers.DateField()
    w_toku = serializers.BooleanField()
    data_zamkniecia = serializers.DateField(required=False)
    id_oddzialu = serializers.SlugRelatedField(queryset=Oddzial.objects.all(), slug_field='nazwa')
    prowadzacy = serializers.SlugRelatedField(queryset=Pracownik.objects.all(), slug_field='nazwisko')
    strony_w_sprawie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='stronywsprawie-detail')

    def validate(self, data):
        if 'data_zamkniecia' in data:
            if data['data_zgloszenia'] > data['data_zamkniecia']:
                raise serializers.ValidationError("Data zgłoszenia musi być wcześniejsza od daty zamknięcia.")
            if data['data_zgloszenia'] > datetime.date.today() or data['data_zamkniecia'] > datetime.date.today():
                raise serializers.ValidationError("Data zgłoszenia lub zamknięcia nie może być z przyszłości.")
            if data['w_toku']:
                raise serializers.ValidationError("Data zamknięcia nie może być dodana, jeśli sprawa jest w toku.")
        elif not data['w_toku']:
            raise serializers.ValidationError("Data zamknięcia jest wymagana, jeśli sprawa nie jest już w toku.")
        return data

    class Meta:
        model = Sprawa
        fields = ['url', 'id_oddzialu', 'opis', 'prowadzacy', 'strona', 'data_zgloszenia', 'w_toku', 'data_zamkniecia',
                  'strony_w_sprawie']


class StronyWSprawieSerializer(serializers.HyperlinkedModelSerializer):
    osoba = serializers.SlugRelatedField(queryset=Obywatel.objects.all(), slug_field='imie')
    sprawa = serializers.SlugRelatedField(queryset=Sprawa.objects.all(), slug_field='opis')

    class Meta:
        model = StronyWSprawie
        fields = ['url', 'RODZAJ', 'sprawa', 'osoba', 'rodzaj']


class SamochodSerializer(serializers.HyperlinkedModelSerializer):
    # szkody = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='SzkodaDetail')
    szkoda = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='szkoda-detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    def validate_rok_prod(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Rok produkcji nie może być z przyszłości.")

    class Meta:
        model = Samochod
        fields = ['url', 'nr_rejestracyjny', 'marka', 'model', 'rok_prod', 'silnik', 'ubezpieczenie', 'szkoda', 'owner']


class SzkodaSerializer(serializers.HyperlinkedModelSerializer):
    samochod = serializers.SlugRelatedField(queryset=Samochod.objects.all(), slug_field='nr_rejestracyjny')

    class Meta:
        model = Szkoda
        fields = ['url', 'opis', 'odszkodowanie', 'samochod']


class UserSamochodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Samochod
        fields = ['url', 'nr_rejestracyjny']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    samochod = UserSamochodSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'samochod']