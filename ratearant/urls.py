from django.urls import path
from . import views

app_name = 'ratearant'
urlpatterns = [
    path('', views.index, name='index'),
]