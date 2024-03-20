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
        
class ChangeUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'password')

class ReviewForm(forms.ModelForm):
    foodRating = forms.IntegerField(label='Food Rating', required=True, max_value=5, min_value=1)
    serviceRating = forms.IntegerField(label='Service Rating', required=True, max_value=5, min_value=1)
    overallRating = forms.IntegerField(label='Overall Rating', required=True, max_value=5, min_value=1)
    message = forms.CharField(required=True, label='', widget=forms.Textarea(attrs={'rows': 5, 'placeholder':'Add your thoughts here!'}))

    class Meta:
        model = Review
        fields = ('foodRating', 'serviceRating', 'overallRating', 'message')

class RestaurantForm(forms.ModelForm):
    name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    website = forms.CharField(required=True)
    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'phone', 'website', 'cuisine')