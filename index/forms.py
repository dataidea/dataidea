from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'shadow form-control form-control-lg', 
                'placeholder': 'Your Name',
                'id': 'inputName'
                }
        )
    )

    email = forms.EmailField(required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'shadow form-control form-control-lg', 
                'placeholder': 'Your Email',
                'id': 'inputName'
                }
        )
    )

    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'shadow form-control form-control-lg', 
                'placeholder': 'Your Subject',
                'id': 'inputSubject'
                }
        )
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'shadow form-control form-control-lg', 
                'placeholder': 'Your Name',
                'id': 'inputName'
                }
        )
    )

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']