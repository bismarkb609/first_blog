
from django import forms
from .models  import Post, UserAccount

class SignUpform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = UserAccount
        fields = [
            'firstName',
            'lastName',
            'userName',
            'Email',
            'password',
            'confirm_password'
        ]



class Loginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = UserAccount
        fields = [ 
            'userName', 
            'password'
        ]


class createPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'published_date']
