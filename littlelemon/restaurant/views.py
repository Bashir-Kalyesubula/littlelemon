from django.shortcuts import render 
from rest_framework import generics 
from rest_framework.decorators import api_view 
from .serializers import MenuSerializer,BookingSerializer 
from . models import Bookingtable,Menutable 

# Create your views here.
def index(request): 
    return render(request, 'index.html', {}) 

class BookingView(generics.ListCreateAPIView):
    queryset = Bookingtable.objects.all()  
    serializer_class = BookingSerializer  
    
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menutable.objects.all() 
    serializer_class = MenuSerializer 
    
class SingleMenuitemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menutable.objects.all() 
    serializer_class = MenuSerializer 