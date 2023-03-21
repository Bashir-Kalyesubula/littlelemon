from django.test import TestCase 
from rest_framework.test import APIClient 
from restaurant.models import Menutable 
from restaurant.serializers import MenuSerializer  
    

class MenuViewTest(TestCase): 
    
    def setUp(self):
        self.client = APIClient() 
        self.menu1 = Menutable.objects.create(title="Rice and Beans",price="6.90",inventory=12) 
        self.menu2 = Menutable.objects.create(title="Matooke",price="8.95",inventory=13) 
        
    def test_getall(self):
        response = self.client.get('/restaurant/menu/') 
        menu = Menutable.objects.all() 
        serializer = MenuSerializer(menu,many=True) 
        self.assertEqual(response.data,serializer.data) 
    