from django.db import models
from inventory.models import Inventory

# Create your models here.
CHOICES = (('kg', 'kg'),
           ('gm', 'gm'),
           ('piece', 'piece'),
           ('ml', 'ml'),
           ('liter', 'liter'),
           ('plate', 'plate'),)
class Menu(models.Model):
    food_name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.food_name}={self.price}"
    
class Recipe(models.Model):
    food_item = models.ForeignKey(Menu,on_delete=models.CASCADE)
    ingredients=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    recipe_quantity=models.FloatField()
    unit=models.CharField(max_length=100,choices=CHOICES)

    def __str__(self):
        return f"{self.food_item} {self.ingredients} {self.recipe_quantity} {self.unit}"