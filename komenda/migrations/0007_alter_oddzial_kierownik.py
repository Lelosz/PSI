# Generated by Django 4.1.3 on 2022-11-21 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('komenda', '0006_alter_oddzial_kierownik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oddzial',
            name='kierownik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='komenda.pracownik'),
        ),
    ]