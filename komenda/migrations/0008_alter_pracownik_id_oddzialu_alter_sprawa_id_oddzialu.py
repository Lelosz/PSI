# Generated by Django 4.1.3 on 2022-11-21 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('komenda', '0007_alter_oddzial_kierownik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pracownik',
            name='id_oddzialu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='komenda.oddzial'),
        ),
        migrations.AlterField(
            model_name='sprawa',
            name='id_oddzialu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='komenda.oddzial'),
        ),
    ]