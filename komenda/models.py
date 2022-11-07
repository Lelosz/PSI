from django.db import models


class Obywatel(models.Model):
    imie = models.CharField(max_length=22)
    nazwisko = models.CharField(max_length=45)
    PESEL = models.CharField(max_length=11)
    adres = models.CharField(max_length=50)
    telefon = models.CharField(max_length=9)


class Pracownik(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=45)
    PESEL = models.CharField(max_length=11)
    adres = models.CharField(max_length=50)
    telefon = models.CharField(max_length=9)
    zarobki = models.DecimalField(max_digits=7, decimal_places=2)
    id_oddzialu = models.ForeignKey('Oddzial', on_delete=models.RESTRICT)


class Oddzial(models.Model):
    nazwa = models.CharField(max_length=45)
    kierownik = models.ForeignKey('Pracownik', on_delete=models.CASCADE)


class Sprawa(models.Model):
    id_oddzialu = models.ForeignKey('Oddzial', on_delete=models.RESTRICT)
    opis = models.TextField()
    prowadzacy = models.ForeignKey(Pracownik, on_delete=models.RESTRICT)
    strona = models.ManyToManyField('Obywatel', through='StronyWSprawie')
    data_zgloszenia = models.DateField(auto_now_add=True)
    w_toku = models.BooleanField(default=True)
    data_zamkniecia = models.DateField(default=None)


class StronyWSprawie(models.Model):
    RODZAJ = (
        ('POS', 'Poszkodowany'),
        ('POD', 'Podejrzany'),
        ('SPR', 'Sprawca'),
        ('SWI', 'Świadek'),
    )
    sprawa = models.ForeignKey(Sprawa, on_delete=models.RESTRICT)
    osoba = models.ForeignKey(Obywatel, on_delete=models.RESTRICT)
    rodzaj = models.CharField(max_length=3, choices=RODZAJ)


class Samochod(models.Model):
    nr_rejestracyjny = models.CharField(max_length=7)
    marka = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    rok_prod = models.IntegerField()
    silnik = models.CharField(max_length=15)
    ubezpieczenie = models.TextField()


class Szkoda(models.Model):
    opis = models.TextField()
    odszkodowanie = models.DecimalField(max_digits=8, decimal_places=2)
    samochod = models.ForeignKey(Samochod, on_delete=models.RESTRICT)
