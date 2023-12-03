from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mt-3', 
                'placeholder': 'Username',
                'id': 'username'
                }
        )
    )

    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control mt-3', 
                'placeholder': 'Email eg johndoe@co.com',
                'id': 'email'
                }
        )
    )

    password1 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mt-3', 
                'placeholder': 'Password',
                'id': 'password'
                }
        )
    )

    password2 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mt-3', 
                'placeholder': 'Confirm password',
                'id': 'password'
                }
        )
    )

    class Meta:
        model = User  # Replace 'User' with your custom User model if you have one
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Username',
                'id': 'username'
                }
        )
    )

    password = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Password',
                'id': 'password'
                }
        )
    )

    class Meta:
        model = User  # Replace 'User' with your custom User model if you have one
        fields = ('username', 'password')