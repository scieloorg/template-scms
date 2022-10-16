# Generated by Django 3.2.12 on 2022-09-02 13:41

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
            name='OfficialJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Official Title')),
                ('foundation_year', models.CharField(blank=True, max_length=4, null=True, verbose_name='Foundation Year')),
                ('ISSN_print', models.CharField(blank=True, max_length=9, null=True, verbose_name='ISSN Print')),
                ('ISSN_electronic', models.CharField(blank=True, max_length=9, null=True, verbose_name='ISSN Eletronic')),
                ('ISSNL', models.CharField(blank=True, max_length=9, null=True, verbose_name='ISSNL')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='officialjournal_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officialjournal_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
