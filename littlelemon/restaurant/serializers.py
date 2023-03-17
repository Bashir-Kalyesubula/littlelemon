from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Bookingtable,Menutable  


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookingtable 
        fields = '__all__'
        
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menutable
        fields = ["title","price","inventory"]
         

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['username','email','groups']