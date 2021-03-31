from django import forms
from django.forms import ModelForm
from .models import UserModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm


""" start registration form here. """
# Registration form.
class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control rounded-0', 'placeholder': 'Username'}))
    email = forms.CharField(max_length=30, widget=forms.EmailInput(attrs={"type":"email", "class":"form-control rounded-0", 'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control rounded-0', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control rounded-0', 'placeholder': 'Confirm password'}))

    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']


""" start signin form here. """
# signin form.
class SigninForm(AuthenticationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control rounded-0', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control rounded-0', 'placeholder': 'Password'}))

    class Meta:
        model  = User
        fields = ['username', 'password']


""" start edit profile form here. """
# EditProfileForm form.
class EditProfileForm(UserChangeForm):

    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'password': 'Password'
        }

        widgets = { 
            'username': forms.TextInput(attrs={'type': 'text', 'class': 'form-control rounded-0'}),
            'first_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control rounded-0'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control rounded-0'}),
            'email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control rounded-0'})
        }


""" start userform here. """
# userform.
class UserForm(ModelForm):
    
    class Meta:
        model = UserModel
        fields = ['image', 'address', 'phone', 'website']

        labels = {
            'image': 'Profile image',
            'address': 'Address',
            'phone': 'Phone',
            'website': 'Website',
        }

        widgets = { 
            'image': forms.ClearableFileInput(attrs={}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control rounded-0'}),
            'phone': forms.NumberInput(attrs={'type': 'number', 'class': 'form-control rounded-0'}),
            'website': forms.URLInput(attrs={'type': 'url', 'class': 'form-control rounded-0'})
        }