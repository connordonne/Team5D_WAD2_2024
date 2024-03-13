from django import forms
from django.contrib.auth.models import User 
from ratearant.models import UserProfile, Review

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')

class ReviewForm(forms.ModelForm):
    message = forms.CharField(required=True)
    foodRating = forms.IntegerField(required=True, max_value=5)
    serviceRating = forms.IntegerField(required=True, max_value=5)
    overallRating = forms.IntegerField(required=True, max_value=5)
    class Meta:
        model = Review
        fields = ('message', 'foodRating', 'serviceRating', 'overallRating')