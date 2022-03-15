from django import forms
from django.forms import TextInput
from django.forms import ModelForm
from ..technology.models import Sfh, Mfh, Commercial, Tos, BuildingProfile
#from .models import Technology

#from .models import Heatpump

class BuildingProfileForm(forms.ModelForm):


    class Meta:
        model = BuildingProfile
        fields = '__all__'
        widgets = {
            'building_type':TextInput(attrs={
                 'class':'form-check-input',
                  'list':'building_type',
                  'name':'building_type',
                   'id':'building_type_list',
                   'style':'width: 150px; margin-left:15px',
            }),


            'numofusers': TextInput(attrs={
                'class': "form-control",
                'name': 'numofusers',
                'id': 'numofusers',
                'max': '6',
                'min':'1',
                'value': "2",
                'onchange':'numofusersr.value = numofusers.value'
            }),
            'electricalenergyconsumptioni': TextInput(attrs={
                'class':'form-control',
                'id':'electricalenergyconsumptioni',
                'name':'electricalenergyconsumptioni',
                'max':'8000',
                'min':'2000',
                'value':'4000',
                'onchange':'electricalenergyconsumptionr.value = electricalenergyconsumptioni.value'
        }),

        'dhwenergyconsumptioni':TextInput(attrs={
        'class':'form-control',
        'id':'dhwenergyconsumptioni',
        'name':'dhwenergyconsumptioni',
         'max':'8000',
         'min':'2000',
         'value':'3000',
        'onchange':'dhwenergyconsumptionr.value = dhwenergyconsumptioni.value'

        }),


        'buildingsizei':TextInput(attrs={
            'class':'form-control',
            'id':'buildingsizei',
            'name':'buildingsizei',
            'max':'250',
            'min':'100',
            'value':'120',
            'onchange':'buildingsizer.value = buildingsizei.value'

        })

        }


class SfhForm(forms.ModelForm):
    numofpersons = forms.IntegerField()
    electricalenergyconsumption = forms.IntegerField()
    dhwenergyconsumption = forms.IntegerField()
    buildingsize = forms.IntegerField()

    class Meta:
        model = Sfh
        fields = ['numofpersons', 'electricalenergyconsumption', 'dhwenergyconsumption', 'buildingsize']


class MfhForm(forms.ModelForm):
    numofdwellings = forms.IntegerField()
    thermalbuildingstandard = forms.IntegerField()
    electricalenergyconsumption = forms.IntegerField()
    dhwenergyconsumption = forms.IntegerField()
    buildingsize = forms.IntegerField()
    class Meta:
                model = Mfh
                fields = ['numofdwellings', 'thermalbuildingstandard', 'electricalenergyconsumption', 'dhwenergyconsumption', 'buildingsize']

class CommercialForm(forms.ModelForm):
        electricalenergyconsumption = forms.IntegerField()
        electricalenergyprofiletype = forms.CharField()
        thermalbuildingtype = forms.IntegerField()
        buildingsize = forms.IntegerField()

        class Meta:
            model = Commercial
            fields = ['electricalenergyconsumption', 'electricalenergyprofiletype','thermalbuildingtype', 'buildingsize']

class TosForm(forms.ModelForm):
    #installedgenpower = forms.IntegerField()
    #azimut = forms.IntegerField()
    #elevation = forms.IntegerField()
    #ratedinverterpowe = forms.IntegerField()
    #chpcombinedheatpower = forms.CharField()
    #chpoperationstrategy = forms.CharField()
    #heatpumptechnology = forms.CharField()
    ##thermalpowerneeded = models.CharField(max_length=20, null=True)
    #heatpumpmodel = forms.CharField()
    #bsfeedinlimitation = forms.FloatField()
    #bsusablecapacity = forms.FloatField()
    #bsratedpower = forms.FloatField()
    #hsusablecapacity = forms.IntegerField()
    #hsratedpower = forms.IntegerField()
    #elvehiclesdistance = forms.IntegerField()

    class Meta:
                model = Tos
                fields = '__all__'
                #fields = ['installedgenpower','azimut','elevation','ratedinverterpower','chpcombinedheatpower', 'chpoperationstrategy','heatpumptechnology','heatpumpmodel','bsfeedinlimitation','bsusablecapacity','bsratedpower','hsusablecapacity','hsratedpower','elvehiclesdistance']

        #'thermalpower'
#class HeatpumpForm(forms.ModelForm):
 #   class Meta:
  #      model = Heatpump
   #     fields = ['technology', 'model']
#'thermalpower'
#class GasheaterForm(forms.ModelForm):
    #class Meta:
        #model = Gasheater
        #fields = ['termalpowerneeded']

#class ParameterForm(forms.ModelForm):
            #class Meta:
               # model = Parameters
                #fields = ['termalpowerneeded']