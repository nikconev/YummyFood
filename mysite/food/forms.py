from django import forms

from mysite.food.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc','item_price','item_image']