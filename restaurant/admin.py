
# Register your models here.
from django.contrib import admin
from .models import *
admin.site.register(Ingredient)
admin.site.register(Menu)
admin.site.register(OrderItem)
admin.site.register(RecipeRequirement)