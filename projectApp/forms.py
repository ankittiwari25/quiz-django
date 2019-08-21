from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}), required=True)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"enter your password",'class': 'form-control'}),required=True)
    con_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"placeholder": "confirm your password", 'class': 'form-control'}), required=True)

    class Meta():
        model = Register
        fields = "__all__"

class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}), required=True)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"enter your password",'class': 'form-control'}),required=True)


    

