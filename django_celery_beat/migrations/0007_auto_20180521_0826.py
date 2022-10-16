# Generated by Django 1.10.7 on 2018-05-21 08:26
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0006_auto_20180322_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodictask',
            name='one_off',
            field=models.BooleanField(default=False,
                                      verbose_name='one-off task'),
        ),
        migrations.AddField(
            model_name='periodictask',
            name='start_time',
            field=models.DateTimeField(blank=True,
                                       null=True,
                                       verbose_name='start_time'),
        ),
    ]
