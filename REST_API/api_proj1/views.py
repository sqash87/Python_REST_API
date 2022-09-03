
# This is an endpoint which means this function will accepet an url request.
import re
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api_proj1 import serializers

#View decorator function which lets me access 'GET', 'POST', 'DELETE', 'UPDATE
@api_view(['GET', 'POST'])

#Accept url request
def drink_list(request, format=None):
    
    #Checking the type of request
    if request.method =='GET':
        #Get the Queryset from the database
        drinks= Drink.objects.all()
        
        # First pass that Queryset drinks into the DrinkSerializer class
        # which converts the Queryset into native python datatype and return it as a serializer.
        serializer=  DrinkSerializer(drinks, many=True)
       
        #Then the serializer data is sent to Response() function to render into json format for the API Incoming calls.
        return Response(serializer.data)
    
    #Creating a data in the databse.
    if request.method== 'POST':
        
        #Getting python native dataset as a serializer by passing the new data inside the serilaizer class.
        serializer = DrinkSerializer(data=request.data)
        
        #Checking is the returned serializer is valid.
        if serializer.is_valid():
            #Save it to the databse.
            serializer.save()
            #return the data to render into JSON for the incoming API Calls
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
#Accepting url request for an individul item with unique PK.
def drink_detail(request, id, format=None): 
    #Getting queryset.
    try:
       drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #For Read Request
    if request.method =='GET':
        #returning python native data type as a serializer.
        serializer= DrinkSerializer(drink)
        #returning to function for rendering into JSON.
        return Response(serializer.data)
    
    #For Update request
    elif request.method == 'PUT': 
        #returning python native data type as a serializer.
        serializer= DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            #Save it to the databse.
            serializer.save()
            #returning to function for rendering into JSON.
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #Deleting request.
    elif request.method =='DELETE':
        #Dlete the data in the database.
         drink.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
        


