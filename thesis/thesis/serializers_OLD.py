from rest_framework import serializers
from ..technology.models import Parameters, Sfh
#


#class SfhSerializer (serializers.ModelSerializer):
 #   class Meta:
  #      model = Sfh
   #     fields ='__all__'

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
         model = Parameters
         fields = '__all__'

class Sfherializer(serializers.ModelSerializer):
    class Meta:
        model = Sfh
        fields = '__all__'