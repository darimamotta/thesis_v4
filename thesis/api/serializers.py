from dataclasses import fields
from rest_framework import serializers
from technology.models import Sfh, Mfh, Commercial, Tos, BuildingProfile
from django.contrib.auth.models import User
from map.models import Search


class BuildingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['first_name', 'last_name', 'email','username']
        fields = '__all__'
        
class TosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tos
        fields = '__all__'

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'