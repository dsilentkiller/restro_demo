from django.db import models

CHOICES = (('kg', 'kg'),
           ('gm', 'gm'),
           ('piece', 'piece'),
           ('ml', 'ml'),
           ('liter', 'liter'),
           ('plate', 'plate'),)




class Inventory(models.Model):
    ingredient_name = models.CharField(max_length=100, default='maida')
    ingredient_quantity = models.FloatField()
    ingredient_price = models.FloatField()
    ingredient_unit = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return f"{self.ingredient_name}={self.ingredient_quantity} {self.ingredient_unit},{self.ingredient_price}"
    

