from rest_framework import serializers
from .models import Obywatel, Pracownik, Oddzial, Sprawa, StronyWSprawie, Samochod, Szkoda
from django.contrib.auth.models import User


class ObywatelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Obywatel
        fields = ['imie','nazwisko','PESEL','adres','telefon']


class PracownikSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pracownik
        fields = ['imie','nazwisko','PESEL','adres','telefon','zarobki','id_oddzialu']


class OddzialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Oddzial
        fields = ['nazwa','kierownik']


class SprawaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sprawa
        fields = ['id_oddzialu','opis','prowadzacy','strona','data_zgloszenia','w_toku','data_zamkniecia']


class StronyWSprawieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StronyWSprawie
        fields = ['RODZAJ','sprawa','osoba','rodzaj']


class SamochodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Samochod
        fields = ['nr_rejestracyjny','marka','model','rok_prod','silnik','ubezpieczenie']


class SzkodaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Szkoda
        fields = ['opis','odszkodowanie','samochod']
