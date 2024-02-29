from django import forms
from Work.models import Mobile
from django.contrib.auth.models import User


class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'

        widgets={
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "year":forms.TextInput(attrs={"class":"form-control"}),
            "color":forms.TextInput(attrs={"class":"form-control"})
            

        }
class Register(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

        
        

class Signin(forms.Form):
    username=forms.CharField()
    password=forms.CharField()