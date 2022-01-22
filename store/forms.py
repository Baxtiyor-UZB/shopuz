from django.forms import ModelForm
from .models import ShippingAddress

class ShippingForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('recepient_fullname','phone_no','address_line1','address_line2','city','state','country')
        labels= {'recepient_fullname':'Ism Familya Sharif','phone_no':'Telefon raqamingiz','address_line1':'Email addres','address_line2':'Viloyat','city':'Tuman','state':'Mahalla','country':'Uy'}
        
        exclude = ['user']


class ShippingUpdateForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('recepient_fullname','phone_no','address_line1','address_line2','city','state','country')
        labels= {'recepient_fullname':'Ism Familya Sharif','phone_no':'Telefon raqamingiz','address_line1':'Email addres','address_line2':'Viloyat','city':'Tuman','state':'Mahalla','country':'Uy'}
        
        exclude = ['user']
