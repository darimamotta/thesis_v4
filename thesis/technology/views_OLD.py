
from plotly.offline import plot
from plotly.graph_objs import Scatter
from django.shortcuts import render,redirect
#from .forms import HeatpumpForm
from .forms import SfhForm, MfhForm, CommercialForm, TosForm, BuildingProfileForm
from .models import Sfh, Mfh, Commercial, Tos, BuildingProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import ParameterSerializer
from django.utils.datastructures import MultiValueDict
from django.contrib import messages
from django.http import JsonResponse
import requests
import json

# Create your views here.
def index(request):
      #HttpResponse "Hello World"
      return render(request, 'index.html')
      #return HttpResponse("<h1> The Record exists in the database! " )

def page2(request):

    return render(request,'page2.html' )

#def sfh2(request):

    #return render(request,'sfh2.html' )
#def mfh2(request):

    #return render(request,'mfh2.html' )
#def commercial(request):

    #return render(request,'commercial.html' )
def page1(request):

    return render(request,'page1.html' )

def page21(request):

    return render(request,'page21.html' )
#def tos(request):

    #return render(request,'tos.html' )
def photo(request):

    return render(request,'photo.html' )

def pump(request):

    return render(request,'pump.html' )
def battery(request):

    return render(request,'battery.html' )
def comb(request):

    return render(request,'comb.html' )
def gas(request):

    return render(request,'gas.html' )
def electric(request):

    return render(request,'electric.html' )
def hydro(request):

    return render(request,'hydro.html' )





def page3(request):
    return render(request, 'page3.html')





def sfhform(request):
    form = SfhForm(request.POST)
    # if form.is_valid():
    if request.method == 'POST':
        Sfh.objects.create(numofpersons = request.POST.get("numofpersonsi"),
        electricalenergyconsumption =request.POST.get("electricalenergyconsumptioni"),
        dhwenergyconsumption = request.POST.get("dhwenergyconsumptioni"),
        buildingsize =request.POST.get("buildingsizei"),)

        return render(request, 'tos.html')

    return render(request, 'sfh2.html')

def mfhform(request):
    form = MfhForm(request.POST)

    if request.method == 'POST':
        Mfh.objects.create(numofdwellings= request.POST.get("numofdwellings"),
                           thermalbuildingstandard=request.POST.get("thermalbuildingstandard"),
        electricalenergyconsumption =request.POST.get("electricalenergyconsumption"),
        dhwenergyconsumption= request.POST.get("dhwenergyconsumption"),
        buildingsize =request.POST.get("buildingsize"),)


        return render(request, 'tos.html')

    return render(request, 'mfh2.html')



def commercialform(request):
    form = CommercialForm(request.POST)

    if request.method == 'POST':
        Commercial.objects.create(electricalenergyconsumption= request.POST.get("electricalenergyconsumption"),
                           electricalenergyprofiletype=request.POST.get("electricalenergyprofiletype"),
        thermalbuildingtype =request.POST.get("thermalbuildingtype"),
        buildingsize =request.POST.get("buildingsize"),)


        return render(request, 'tos.html')

    return render(request, 'commercial.html')


def tosform(request):
    form = TosForm(request.POST)
    if request.method == 'POST':
        Tos.objects.create(name=request.POST.get('name'),
            installedgenpower=request.POST.get("installedgenpower"),
                           azimut=request.POST.get("azimut"),
                           elevation=request.POST.get("elevation"),
                           ratedinverterpower=request.POST.get("ratedinverterpower"),
                           chpcombinedheatpower=request.POST.get("chpcombinedheatpower"),
                           chpoperationstrategy=request.POST.get("chpoperationstrategy"),
                           heatpumptechnology=request.POST.get("heatpumptechnology"),
                           heatpumpmodel=request.POST.get("heatpumpmodel"),
                           bsfeedinlimitation=request.POST.get("bsfeedinlimitation"),
                           bsusablecapacity=request.POST.get("bsusablecapacity"),
                           bsratedpower=request.POST.get("bsratedpower"),
                           hsusablecapacity=request.POST.get("hsusablecapacity"),
                           hsratedpower=request.POST.get("hsratedpower"),
                           elvehiclesdistance=request.POST.get("elvehiclesdistance"),)


        return render(request, 'page3.html')

    return render(request, 'tos.html')





def input(request):
    sfhpar = [{'numofusers': '2', 'electricalenergyconsumption': '50','dhwenergyconsumption': '1000', 'buildingsize': '120'}]

    return JsonResponse ({'sfh_parameters': sfhpar}, safe=False)
        #return JsonResponse({'numofpersons':'numofpersons', 'electricalenergyconsumption':'electricalenergyconsumption','dhwenergyconsumption':'dhwenergyconsumption', 'buildingsize':'buildingsize'})





# In production, this should be set as an environment variable


def space(request):
    res = requests.get(f"http://api.open-notify.org/astros.json")
    return JsonResponse(res.json())