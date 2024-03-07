from django import forms
from django.contrib.auth.models import User 
from ratearant.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')
