
from django import forms
from django import forms

class SignUpform(forms.Form):
    Firstname = forms.CharField(label="FirstName", max_length=200, required=True)
    Othername = forms.CharField(label="OtherName", max_length=200, required=False)
    LastName = forms.CharField(label="LastName", max_length=200, required=True) 
    username = forms.CharField(label="UserName", max_length=100)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", required=True)
    confirm_password = forms.CharField(label="Confirm Password", required=True)



class Loginform(forms.Form):
    username = forms.CharField(label="UserName", max_length=200)
    password = forms.CharField(label="Password")