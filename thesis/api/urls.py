from . import views

from django.urls import path

app_name ="api"
urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('list-buildingProfile/', views.buildingProfileList, name='list-buildingProfile'),
    path('list-search/', views.searchList, name='list-search'),
    path('list-tos/', views.tosList, name='list-tos'),
    #path('list-all/<int:user_id>', views.allList, name='list-all'),
    path('list-all/', views.allList, name='list-all'),
    path('res-api/', views.apiResults, name='apiResults'),
]