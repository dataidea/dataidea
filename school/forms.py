from django import forms
from .models import LearnerProfile

class LearnerProfileForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mt-3', 
                'placeholder': 'Your Name',
                'id': 'name'
                }
        )
    )

    display_picture = forms.ImageField(
        required=False,
        label='',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control mt-3',
                'id': 'display_picture'
                }
        )
    )

    info = forms.CharField(
        required=False,
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control mt-3',
                'placeholder': 'About You',
                'id': 'info',
                'rows': '10'

                }
        )
    )

    github = forms.URLField(
        required=False,
        label='',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control mt-3',
                'placeholder': 'Github URL',
                'id': 'github'
                }
        )
    )

    linkedin = forms.URLField(
        required=False,
        label='',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control mt-3',
                'placeholder': 'Linkedin URL',
                'id': 'linkedin'
                }
        )
    )

    other = forms.URLField(
        required=False,
        label='',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control mt-3',
                'placeholder': 'Other URL',
                'id': 'other'
                }
        )
    )
    class Meta:
        model = LearnerProfile
        fields = ['name', 'display_picture', 'info', 'github', 'linkedin', 'other']