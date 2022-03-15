"""thesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views

from django.contrib import admin
from django.urls import path, include
# from map import views as map_views
#from .finished_apps import simpleexample

# -> new
app_name = 'technology'
# <-
urlpatterns = [
    path('', views.index, name='thesis-index'),
    path('page21.html', views.page21, name='thesis-page21'),
    path('mfh2.html', views.mfhform, name='mfh-form'),
    path('commercial.html', views.commercialform, name='com-form'),
    path('photo.html', views.photo, name='photo'),
    path('comb.html', views.comb, name='comb'),
    path('gas.html', views.gas, name='gas'),
    path('electric.html', views.electric, name='electric'),
    path('pump.html', views.pump, name='pump'),
    path('hydro.html', views.hydro, name='hydro'),
    path('battery.html', views.battery, name='battery'),
    path('page1.html', views.page1, name='thesis-page1'),
    path('page2.html', views.page2, name='thesis-page2'),
    path('page3', views.page3, name='thesis-page3'),
    # -> new
    # path('space/', views.space, name='space'),
    # path('inputjson/', views.input, name='input'),
    path('tos', views.tosform, name='tos'),
    path('show-json-test', views.show_json_test, name='show-json-test'),
    path('create-building/', views.create_building_profile, name='create-building')

    # <-


]

