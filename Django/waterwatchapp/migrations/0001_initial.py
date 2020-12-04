# Generated by Django 2.2.7 on 2019-11-29 03:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterConsumption',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Suburb', models.CharField(max_length=100)),
                ('NoOfSingleResProp', models.IntegerField()),
                ('AvgMonthlyKL', models.IntegerField()),
                ('AvgMonthlyKLPredicted', models.IntegerField()),
                ('PredictionAccuracy', models.IntegerField()),
                ('Month', models.CharField(max_length=50)),
                ('Year', models.IntegerField()),
                ('DateTime', models.DateTimeField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'WaterConsumption',
            },
        ),
    ]
