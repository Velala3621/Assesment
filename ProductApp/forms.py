from django.forms import ModelForm, inlineformset_factory
from .models import Product, Productitem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['first_name','last_name','username','email','password1','password2',]


class ProductForm(forms.ModelForm):
    image=forms.FileField()
    class Meta:
        model = Product
        fields = '__all__'
    def clean_image(self):
        print("this is from clean form")
        image=self.cleaned_data['image']



class ProductItemForm(ModelForm):
    class Meta:
        model = Productitem
        exclude = ()


ProductItemFormset = inlineformset_factory(Product, Productitem,
                                            form=ProductItemForm, extra=1)
