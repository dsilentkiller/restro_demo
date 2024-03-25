from django import forms
from order.models import Order, Table


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {


            'order_quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'price': forms.TextInput(attrs={'class': 'forms.control'}),
            # # 'unit': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
            # 'description': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'category': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
            # 'table': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
        }


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


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('__all__')
        widgets = {
            'table_name': forms.TextInput(attrs={'class': 'forms.control'}),
            'floor': forms.TextInput(attrs={'class': 'forms.control'})
        }
