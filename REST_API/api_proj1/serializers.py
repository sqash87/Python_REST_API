
#from python object to json
from dataclasses import field
from rest_framework import serializers
from .models import Drink

#Serializers allow complex data such as querysets and model instances 
#to be converted to native Python datatypes 
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']