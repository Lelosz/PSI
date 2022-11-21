from django.urls import path, include
from . import views

urlpatterns = [
    path(r'obywatel/', views.ObywatelList.as_view(), name=views.ObywatelList.name),
    path(r'pracownik/', views.PracownikList.as_view(), name=views.PracownikList.name),
    path(r'oddzial/', views.OddzialList.as_view(), name=views.OddzialList.name),
    path(r'sprawa/', views.SprawaList.as_view(), name=views.SprawaList.name),
    path(r'stronywsprawie/', views.StronyWSprawieList.as_view(), name=views.StronyWSprawieList.name),
    path(r'samochod/', views.SamochodList.as_view(), name=views.SamochodList.name),
    path(r'szkoda/', views.SzkodaList.as_view(), name=views.SzkodaList.name),
    path('api-auth/', include('rest_framework.urls')),

]
