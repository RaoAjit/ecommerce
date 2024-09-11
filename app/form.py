from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import customer
from django.contrib.auth.forms import UsernameField

class userregi(UserCreationForm):
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='password1',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='password2',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(label='email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','password1','password2','email']

class chpassword(PasswordChangeForm):
    old_password=forms.CharField(label=_('oldpassword'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))   
    new_password1=forms.CharField(label=_('newpassword1'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())                              
    new_password2=forms.CharField(label=_('newpassword2'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'})) 

class passwordre(PasswordResetForm):
    email=forms.CharField(label=_('Email'),max_length=240,widget=forms.EmailInput(attrs={'autocomoplete':'email','class':'form-control'}))

class adressform(forms.ModelForm):
    class Meta:
        model=customer
        fields=['name','locality','city','zipcode','state']
        widgets={'name':forms.TextInput({"class":'form-control'}),
                 'locality':forms.TextInput({"class":'form-control'}),
                 'city':forms.TextInput({"class":'form-control'}),
                 'zipcode':forms.NumberInput({"class":'form-control'}),
                 'state':forms.Select({"class":'form-control'})}


class loginn(AuthenticationForm):
     username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
     password=forms.CharField(label=_('password'),widget=forms.PasswordInput(attrs={'autocomplete':'currnet-password','class':'form-control'}))


   
                 

                 



                          