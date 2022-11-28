from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path(r'obywatel/', views.ObywatelList.as_view(), name=views.ObywatelList.name),
    path('obywatel/<int:pk>', views.ObywatelDetail.as_view(), name=views.ObywatelDetail.name),
    path(r'pracownik/', views.PracownikList.as_view(), name=views.PracownikList.name),
    path('pracownik/<int:pk>', views.PracownikDetail.as_view(), name=views.PracownikDetail.name),
    path(r'oddzial/', views.OddzialList.as_view(), name=views.OddzialList.name),
    path('oddzial/<int:pk>', views.OddzialDetail.as_view(), name=views.OddzialDetail.name),
    path(r'sprawa/', views.SprawaList.as_view(), name=views.SprawaList.name),
    path('sprawa/<int:pk>', views.SprawaDetail.as_view(), name=views.SprawaDetail.name),
    path(r'stronywsprawie/', views.StronyWSprawieList.as_view(), name=views.StronyWSprawieList.name),
    path('stronywsprawie/<int:pk>', views.StronyWSprawieDetail.as_view(), name=views.StronyWSprawieDetail.name),
    path(r'samochod/', views.SamochodList.as_view(), name=views.SamochodList.name),
    path('samochod/<int:pk>', views.SamochodDetail.as_view(), name=views.SamochodDetail.name),
    path(r'szkoda/', views.SzkodaList.as_view(), name=views.SzkodaList.name),
    path('szkoda/<int:pk>', views.SzkodaDetail.as_view(), name=views.SzkodaDetail.name),
    path('api-auth/', include('rest_framework.urls')),

]
