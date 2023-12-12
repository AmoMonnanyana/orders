from django import forms
from .models import products, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'customer','quantity_ordered']

class UpdateStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    fields = ['order_id']
    new_status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))