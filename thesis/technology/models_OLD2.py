from django.db import models

# Create your models here.
from django.db import models




class Sfh(models.Model):
    #id = models.ForeignKey(map.Search.id, blank=True, null=True)
    numofpersons = models.IntegerField(null=True)
    electricalenergyconsumption = models.IntegerField(null=True)
    dhwenergyconsumption = models.IntegerField(null=True)
    buildingsize = models.IntegerField(null=True)

    #def __str__(self):
       #return {'numofpersons':self.numofpersons, 'electricalenergyconsumption':self.electricalenergyconsumption, 'dhwenergyconsumption':self.dhwenergyconsumption,'buildingsize':self.buildingsize}

    #class Meta:
        #ordering = ['numofpersons']

class Mfh(models.Model):
   #id = models.ForeignKey(map.Search.id, blank=True, null=True)
    numofdwellings = models.IntegerField(null=True)
    thermalbuildingstandard = models.IntegerField(null=True)
    electricalenergyconsumption= models.IntegerField(null=True)
    dhwenergyconsumption = models.IntegerField(null=True)
    buildingsize = models.IntegerField(null=True)

class Commercial(models.Model):
    #id = models.ForeignKey(map.Search.id, blank=True, null=True)
    electricalenergyconsumption = models.IntegerField(null=True)
    electricalenergyprofiletype = models.CharField(max_length=20, null=True)
    thermalbuildingtype = models.IntegerField(null=True)
    buildingsize = models.IntegerField(null=True)


class Tos(models.Model):
    #id = models.ForeignKey(map.Search.id, blank=True, null=True)
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