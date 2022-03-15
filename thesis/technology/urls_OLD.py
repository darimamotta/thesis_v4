
from . import views

from django.contrib import admin
from django.urls import path, include
# from map import views as map_views
#from .finished_apps import simpleexample


# -> new
app_name = 'technology'
# <-
urlpatterns = [
    path('', views.home),
    path('page21.html', views.page21, name='thesis-page21'),
    #path('sfh2.html', views.sfh2, name='thesis-sfh2'),
    path('sfh2.html', views.sfhform, name='sfh-form'),
    path('mfh2.html', views.mfhform, name='mfh-form'),
    #path('mfh2.html', views.mfh2, name='thesis-mfh2'),
    #path('commercial.html', views.commercial, name='thesis-commercial'),
    path('commercial.html', views.commercialform, name='com-form'),
    #path('tos.html', views.tos, name='tos'),
    path('tos.html', views.tosform, name='tos'),
    path('page1.html', views.page1, name='thesis-page1'),
    path('page2.html', views.page2, name='thesis-page2'),
    path('page3.html', views.page3, name='thesis-page3'),
   # path('map.html', map_views.map, name='map'),
    path('api/', include('api.urls')),
    path('space/', views.space, name='space'),
    path('inputjson/', views.input, name='input'),
]