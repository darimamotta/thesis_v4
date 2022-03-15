from django.contrib import admin
#from .models import Gasheater
#from .models import Heatpump, Parameters
from .models import Sfh, Mfh,Commercial,Tos, BuildingProfile

class EntryAdmin(admin.ModelAdmin):
    list_display = ('technology', 'model')
    list_filter = ['model']


class SfhAdmin(admin.ModelAdmin):
    list_display = ('numofpersons', 'electricalenergyconsumption', 'dhwenergyconsumption','buildingsize')
    list_filter = ['numofpersons']



class MfhAdmin(admin.ModelAdmin):
    list_display = ('numofdwellings', 'thermalbuildingstandard', 'electricalenergyconsumption', 'dhwenergyconsumption','buildingsize')
    list_filter = ['numofdwellings']

class Commercialdmin(admin.ModelAdmin):
    list_display = ('electricalenergyconsumption', 'electricalenergyprofiletype', 'thermalbuildingtype','buildingsize')
    list_filter = ['electricalenergyconsumption']

#class Tosadmin(admin.ModelAdmin):
 #   list_display = ('installedgenpower', 'azimut', 'elevation', 'ratedinverterpower', 'chpcombinedheatpower', 'chpoperationstrategy', 'heatpumptechnology', 'heatpumpmodel', 'bsfeedinlimitation', 'bsusablecapacity', 'bsratedpower', 'hsusablecapacity', 'hsratedpower', 'elvehiclesdistance')
  #  list_filter = ['chpcombinedheatpower ']

#class BuildingProfile(admin.ModelAdmin):
 #   list_display = ('technology','numofpersons', 'electricalenergyconsumption', 'energyconsumption', 'buildingsize')
  #  list_filter = ['numofpersons']

# Register your models here.
#admin.site.register(Heatpump)
admin.site.register(Sfh)
admin.site.register(Mfh)
admin.site.register(Commercial)
admin.site.register(Tos)
admin.site.register(BuildingProfile)

#admin.site.register(Gasheater)
#admin.site.register(Mynumber, MynumberAdmin)
admin.site.site_header = "Jülich Dashboard"

