from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Your Name',
                'id': 'name'
                }
        )
    )

    email = forms.EmailField(required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Your Email',
                'id': 'email'
                }
        )
    )

    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Subject',
                'id': 'subject'
                }
        )
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Message',
                'rows': '5'
                }
        )
    )

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']