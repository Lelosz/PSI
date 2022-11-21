from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from komenda.models import Obywatel, Pracownik, Oddzial, Sprawa, StronyWSprawie, Samochod, Szkoda
from komenda.serializers import ObywatelSerializer, PracownikSerializer, OddzialSerializer, SprawaSerializer, StronyWSprawieSerializer, SamochodSerializer, SzkodaSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User
# from .custompermission import IsCurrentUserOwnerOrReadOnly


# class ObywatelList(generics.ListCreateAPIView):
#     queryset = Obywatel.imie.all()
#     serializer_class = ObywatelSerializer
#     name = 'obywatel'
#     filterset_fields = ['imie']
#     search_fields = ['imie']
#     ordering_fields = ['imie']


class ObywatelList(generics.ListCreateAPIView):
    queryset = Obywatel.objects.all()
    serializer_class = ObywatelSerializer
    name = 'obywatel'


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik'


class OddzialList(generics.ListCreateAPIView):
    queryset = Oddzial.objects.all()
    serializer_class = OddzialSerializer
    name = 'oddzial'


class SprawaList(generics.ListCreateAPIView):
    queryset = Sprawa.objects.all()
    serializer_class = SprawaSerializer
    name = 'sprawa'


class StronyWSprawieList(generics.ListCreateAPIView):
    queryset = StronyWSprawie.objects.all()
    serializer_class = StronyWSprawieSerializer
    name = 'stronywsprawie'


class SamochodList(generics.ListCreateAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod'


class SzkodaList(generics.ListCreateAPIView):
    queryset = Szkoda.objects.all()
    serializer_class = SzkodaSerializer
    name = 'szkoda'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'obywatels': reverse(ObywatelList.name, request=request),
                         'pracowniks': reverse(PracownikList.name, request=request),
                         'oddzials': reverse(OddzialList.name, request=request),
                         'sprawas': reverse(SprawaList.name, request=request),
                         'samochods': reverse(SamochodList.name, request=request),
                         'szkodas': reverse(SzkodaList.name, request=request)})



