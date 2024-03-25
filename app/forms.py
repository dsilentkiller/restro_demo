from django import forms
from django import forms
from app.models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {

            

            'order_quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'table_name': forms.TextInput(attrs={'class': 'forms.control'}),



        }


class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('__all__')
        widgets = {
            'menu_item': forms.TextInput(attrs={'class': 'forms.control'}),

            'ingredient': forms.TextInput(attrs={'class': 'forms.control'}),
            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            # # 'unit': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
            # 'description': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'category': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
            # 'table': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
        }


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('__all__')
        widgets = {


            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),

        }


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'forms.control'})
        }


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('__all__')
        widgets = {
            'ingredient_name': forms.TextInput(attrs={'class': 'forms.control'}),
            'available_qty': forms.TextInput(attrs={'class': 'forms.control'}),
            'measurment_unit': forms.TextInput(attrs={'class': 'forms.control'}),
        }
