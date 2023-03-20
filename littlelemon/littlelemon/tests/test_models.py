from django.test import TestCase 
from restaurant.models import Menutable,Bookingtable 

class MenuItemTest(TestCase): 
    
    def test_get_item(self):
        item = Menutable.objects.create(title="Matooke", price=8.95,inventory=13) 
        itemstr = item 
        
        
        self.assertEqual(item, "Rice and Beans : 6.90,12")