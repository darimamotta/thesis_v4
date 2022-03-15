# Generated by Django 3.2.9 on 2022-03-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricalenergyconsumption', models.IntegerField(null=True)),
                ('electricalenergyprofiletype', models.CharField(max_length=20, null=True)),
                ('thermalbuildingtype', models.IntegerField(null=True)),
                ('buildingsize', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mfh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numofdwellings', models.IntegerField(null=True)),
                ('thermalbuildingstandard', models.IntegerField(null=True)),
                ('electricalenergyconsumption', models.IntegerField(null=True)),
                ('dhwenergyconsumption', models.IntegerField(null=True)),
                ('buildingsize', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sfh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numofpersons', models.IntegerField(null=True)),
                ('electricalenergyconsumption', models.IntegerField(null=True)),
                ('dhwenergyconsumption', models.IntegerField(null=True)),
                ('buildingsize', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installedgenpower', models.IntegerField(null=True)),
                ('azimut', models.IntegerField(null=True)),
                ('elevation', models.IntegerField(null=True)),
                ('ratedinverterpower', models.IntegerField(null=True)),
                ('chpcombinedheatpower', models.CharField(max_length=20, null=True)),
                ('chpoperationstrategy', models.CharField(max_length=20, null=True)),
                ('heatpumptechnology', models.CharField(max_length=20, null=True)),
                ('heatpumpmodel', models.CharField(max_length=20, null=True)),
                ('bsfeedinlimitation', models.FloatField(null=True)),
                ('bsusablecapacity', models.FloatField(null=True)),
                ('bsratedpower', models.FloatField(null=True)),
                ('hsusablecapacity', models.IntegerField(null=True)),
                ('hsratedpower', models.IntegerField(null=True)),
                ('elvehiclesdistance', models.IntegerField(null=True)),
            ],
        ),
    ]
