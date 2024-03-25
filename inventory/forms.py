from django import forms
from inventory.models import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('__all__')
        widgets = {
           
            'ingredient_name': forms.TextInput(attrs={'class': 'forms.control'}),

            'ingredient_quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'ingredient_price': forms.TextInput(attrs={'class': 'forms.control'}),
           



        }


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ('__all__')
#         widgets = {
#             'item_name': forms.TextInput(attrs={'class': 'forms.control'}),

#             'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
#             'price': forms.TextInput(attrs={'class': 'forms.control'}),
#             # 'unit': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
#             'description': forms.TextInput(attrs={'class': 'forms.control'}),
#             # 'category': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
#             # 'table': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
#         }


# class PurchaseForm(forms.ModelForm):
#     class Meta:
#         model = Purchase
#         fields = ('__all__')
#         widgets = {


#             'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
#             'price': forms.TextInput(attrs={'class': 'forms.control'}),
#             # 'unit': forms.RadioSelectField(attrs={'class': 'forms.control'}),
#             'description': forms.TextInput(attrs={'class': 'forms.control'}),
#             # 'category': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
#             # 'table': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
#         }


# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ('__all__')
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'forms.control'})
#         }


# class TableForm(forms.ModelForm):
#     class Meta:
#         model = Table
#         fields = ('__all__')
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'forms.control'}),
#             'floor': forms.TextInput(attrs={'class': 'forms.control'})
#         }


# class StockForm(forms.ModelForm):
#     class Meta:
#         model = StockReport
#         fields = ('__all__')
#         widgets = {
#             'menu_item_name': forms.TextInput(attrs={'class': 'forms.control'}),
#             # 'inventory_quantity': forms.TextInput(attrs={'class': 'forms.control'})
#         }
