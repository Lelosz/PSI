from rest_framework import serializers
from .models import Obywatel, Pracownik, Oddzial, Sprawa, StronyWSprawie, Samochod, Szkoda
from django.contrib.auth.models import User


class komendaSerializer(serializers.HyperlinkedModelSerializer):
