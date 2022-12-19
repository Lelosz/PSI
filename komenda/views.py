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
    name = 'obywatel-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)




class ObywatelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obywatel.objects.all()
    serializer_class = ObywatelSerializer
    name = 'obywatel-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)




class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OddzialList(generics.ListCreateAPIView):
    queryset = Oddzial.objects.all()
    serializer_class = OddzialSerializer
    name = 'oddzial-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OddzialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oddzial.objects.all()
    serializer_class = OddzialSerializer
    name = 'oddzial-detail'


class SprawaList(generics.ListCreateAPIView):
    queryset = Sprawa.objects.all()
    serializer_class = SprawaSerializer
    name = 'sprawa-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SprawaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sprawa.objects.all()
    serializer_class = SprawaSerializer
    name = 'sprawa-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StronyWSprawieList(generics.ListCreateAPIView):
    queryset = StronyWSprawie.objects.all()
    serializer_class = StronyWSprawieSerializer
    name = 'stronywsprawie-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StronyWSprawieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StronyWSprawie.objects.all()
    serializer_class = StronyWSprawieSerializer
    name = 'stronywsprawie-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SamochodList(generics.ListCreateAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod-list'


class SamochodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod-detail'


class SzkodaList(generics.ListCreateAPIView):
    queryset = Szkoda.objects.all()
    serializer_class = SzkodaSerializer
    name = 'szkoda-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SzkodaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Szkoda.objects.all()
    serializer_class = SzkodaSerializer
    name = 'szkoda-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'obywatele': reverse(ObywatelList.name, request=request),
                         'pracownicy': reverse(PracownikList.name, request=request),
                         'oddzialy': reverse(OddzialList.name, request=request),
                         'sprawy': reverse(SprawaList.name, request=request),
                         'strony w sprawie': reverse(StronyWSprawieList.name, request=request),
                         'samochody': reverse(SamochodList.name, request=request),
                         'szkody': reverse(SzkodaList.name, request=request)})
