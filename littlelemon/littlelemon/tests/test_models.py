from django.test import TestCase 
from restaurant.models import Menutable,Bookingtable 
from rest_framework.test import APIClient 

class MenuItemTest(TestCase): 
    def setUp(self):
        self.client = APIClient
        self.menu1 = Menutable.objects.create(title="Rice and Beans",price="6.90",inventory=12) 
        self.menu2 = Menutable.objects.create(title="Matooke",price="8.95",inventory=13) 
        
    
    def test_get_item(self):
        menu3 = Menutable.objects.create(title="Peas salad", price="3.50",inventory=34) 
        anticipated_value = f"{menu3.title}:{menu3.price}"
        self.assertEqual(str(menu3),anticipated_value)
        