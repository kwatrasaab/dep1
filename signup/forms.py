from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'First_Name',
            'Last_Name',
            'DOB',
            'Loc',
            'Email',
            'Password',
            'Gender'
        ]
