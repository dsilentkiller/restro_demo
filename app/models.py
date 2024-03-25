
from datetime import timezone
from typing import Any
from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=20)

    price = models.FloatField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    quantity = models.IntegerField()
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Inventory(models.Model):

    ingredient_name = models.CharField(max_length=100)
    available_qty = models.IntegerField()
    measurement_unit = models.CharField(max_length=20)

    def __str__(self):
        return self.ingredient_name


class RecipeRequirement(models.Model):
    menu_item_name = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='recipe')
    ingredient = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.menu_item_name} - {self.quantity}"


class Order(models.Model):
    order_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    table_name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_item.name} - {self.table_name}"
