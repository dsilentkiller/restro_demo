from django.db import models


# Create your models here.


class Table(models.Model):
    table_name = models.CharField(max_length=50)
    floor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.table_name}={self.floor}"

# class Order(models.Model):
#     order_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     order_quantity = models.FloatField()
#     price = models.FloatField()

#     def __str__(self):
#         return f"{self.order_item}={self.order_quantity} &{self.price}"
