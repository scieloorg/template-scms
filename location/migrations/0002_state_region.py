# Generated by Django 3.2.12 on 2022-10-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='region',
            field=models.CharField(blank=True, choices=[('', ''), ('Norte', 'Norte'), ('Nordeste', 'Nordeste'), ('Centro-Oeste', 'Centro-Oeste'), ('Sudeste', 'Sudeste'), ('Sul', 'Sul')], max_length=255, null=True, verbose_name='Region'),
        ),
    ]