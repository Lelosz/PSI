# Generated by Django 4.1.3 on 2023-01-15 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Obywatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=22)),
                ('nazwisko', models.CharField(max_length=45)),
                ('PESEL', models.CharField(max_length=11)),
                ('adres', models.CharField(max_length=50)),
                ('telefon', models.CharField(max_length=9)),
            ],
            options={
                'ordering': ('imie',),
            },
        ),
        migrations.CreateModel(
            name='Oddzial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=20)),
                ('nazwisko', models.CharField(max_length=45)),
                ('PESEL', models.CharField(max_length=11)),
                ('adres', models.CharField(max_length=50)),
                ('telefon', models.CharField(max_length=9)),
                ('zarobki', models.DecimalField(decimal_places=2, max_digits=7)),
                ('id_oddzialu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='komenda.oddzial')),
            ],
        ),
        migrations.CreateModel(
            name='Samochod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_rejestracyjny', models.CharField(max_length=7)),
                ('marka', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=20)),
                ('rok_prod', models.IntegerField()),
                ('silnik', models.CharField(max_length=15)),
                ('ubezpieczenie', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samochod', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sprawa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.TextField()),
                ('data_zgloszenia', models.DateField(auto_now_add=True)),
                ('w_toku', models.BooleanField(default=True)),
                ('data_zamkniecia', models.DateField(default=None)),
                ('id_oddzialu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='komenda.oddzial')),
                ('prowadzacy', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='komenda.pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='Szkoda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.TextField()),
                ('odszkodowanie', models.DecimalField(decimal_places=2, max_digits=8)),
                ('samochod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='komenda.samochod')),
            ],
        ),
        migrations.CreateModel(
            name='StronyWSprawie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj', models.CharField(choices=[('POS', 'Poszkodowany'), ('POD', 'Podejrzany'), ('SPR', 'Sprawca'), ('SWI', 'Świadek')], max_length=3)),
                ('osoba', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='komenda.obywatel')),
                ('sprawa', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='komenda.sprawa')),
            ],
        ),
        migrations.AddField(
            model_name='sprawa',
            name='strona',
            field=models.ManyToManyField(through='komenda.StronyWSprawie', to='komenda.obywatel'),
        ),
        migrations.AddField(
            model_name='oddzial',
            name='kierownik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='komenda.pracownik'),
        ),
    ]
