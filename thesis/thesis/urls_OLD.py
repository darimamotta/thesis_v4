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

from ..technology import views_OLD

from django.contrib import admin
from django.urls import path, include
# from map import views as map_views
#from .finished_apps import simpleexample

urlpatterns = [
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
       #path('', cache_page(60)(views.index), name='dashboard-index'),
    path('admin/', admin.site.urls),
    path('', views_OLD.index, name='thesis-index'),
    path('page21.html', views_OLD.page21, name='thesis-page21'),
    #path('sfh2.html', views.sfh2, name='thesis-sfh2'),
    #path('sfh2.html', views.sfhform, name='sfh-form'),
    # path('create-building/', views.create_building_profile, name='create-building'),
    path('mfh2.html', views_OLD.mfhform, name='mfh-form'),
    #path('mfh2.html', views.mfh2, name='thesis-mfh2'),
    #path('commercial.html', views.commercial, name='thesis-commercial'),
    path('commercial.html', views_OLD.commercialform, name='com-form'),
    path('tos', views_OLD.tosform, name='tos'),
    path('photo.html', views_OLD.photo, name='photo'),
    path('comb.html', views_OLD.comb, name='comb'),
    path('gas.html', views_OLD.gas, name='gas'),
    path('electric.html', views_OLD.electric, name='electric'),
    path('pump.html', views_OLD.pump, name='pump'),
    path('hydro.html', views_OLD.hydro, name='hydro'),
    path('battery.html', views_OLD.battery, name='battery'),
    path('page1.html', views_OLD.page1, name='thesis-page1'),
    path('page2.html', views_OLD.page2, name='thesis-page2'),
    path('page3.html', views_OLD.page3, name='thesis-page3'),
    # path('map', map.views.map, name='map'),
    # -> new
    path('map/', include('map.urls')),
    # <-
    path('api/', include('api.urls')),
    path('space/', views_OLD.space, name='space'),
    path('inputjson/', views_OLD.input, name='input'),
    #path('tos.html', views.tos, name='tos'),
    #path('entry1', views.entry1, name='thesis-entry'),
    #path('parameters-list/', views.parameterList, name='parameters-list'),
    #path('parameters-detail/<str:pk>/', views.parameterDetail, name='parameters-detail'),
    #path('test_plotly.html', views.test, name='test'),
    #path('test_plotly.html', map_views.main1, name='test_plotly'),
    #path('test_plotly.html', map_views.index, name='test_plotly1'),
    #path('test_plotly.html', views.index1, name='test_plotly12'),
    #path('', views.home, name="home"),
    #path('', views.base, name="base")
    path('technology/', include('technology.urls')),


]

