from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

class BuildingProfile(models.Model):
        building_type = models.CharField(max_length=20)
        numofusers = models.IntegerField(null=True)
        electricalenergyconsumptioni = models.IntegerField(null=True)
        dhwenergyconsumptioni = models.IntegerField(null=True)
        buildingsizei = models.IntegerField(null=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Tos(models.Model):

    installedgenpower = models.IntegerField(null=True)
    azimut = models.IntegerField(null=True)
    elevation = models.IntegerField(null=True)
    ratedinverterpower = models.IntegerField(null=True)
    chpcombinedheatpower = models.CharField(max_length=20, null=True)
    chpoperationstrategy = models.CharField(max_length=20, null=True)
    heatpumptechnology = models.CharField(max_length=20, null=True)
    #thermalpowerneeded = models.CharField(max_length=20, null=True)
    heatpumpmodel=models.CharField(max_length=20, null=True)
    bsfeedinlimitation=models.FloatField(null=True)
    bsusablecapacity=models.FloatField(null=True)
    bsratedpower=models.FloatField(null=True)
    hsusablecapacity=models.IntegerField(null=True)
    hsratedpower=models.IntegerField(null=True)
    elvehiclesdistance= models.IntegerField(null=True)
    # -> new
    building = models.ForeignKey(BuildingProfile, on_delete=models.CASCADE, null=True)
    # <-

# class User (AbstractUser): 
#     pass

# To DELETE!
class Sfh(models.Model):
    #id = models.IntegerField(primary_key=True)
    #id = models.ForeignKey(Search.id, blank=True, null=True)
    numofpersons = models.IntegerField(null=True)
    electricalenergyconsumption = models.IntegerField(null=True)
    dhwenergyconsumption = models.IntegerField(null=True)
    buildingsize = models.IntegerField(null=True)


#class Meta:
 #   managed = True
  #  db_table = 'Sfh'

class Mfh(models.Model):
    #id = models.IntegerField(primary_key=True)
   #id = models.ForeignKey(Search.id, blank=True, null=True)
    numofdwellings = models.IntegerField(null=True)
    thermalbuildingstandard = models.IntegerField(null=True)
    electricalenergyconsumption= models.IntegerField(null=True)
    dhwenergyconsumption = models.IntegerField(null=True)
    buildingsize = models.IntegerField(null=True)

class Commercial(models.Model):
    #id = models.IntegerField(primary_key=True)
    #id = models.ForeignKey(Search.id, blank=True, null=True)
    electricalenergyconsumption = models.IntegerField(null=True)
    electricalenergyprofiletype = models.CharField(max_length=20, null=True)
    thermalbuildingtype = models.IntegerField(null=True)
    buildingsize = models.IntegerField(null=True)

