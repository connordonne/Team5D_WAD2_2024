from django.urls import path
from . import views

app_name = 'ratearant'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('restaurant/<slug:restaurant_name_slug>/',
         views.show_restaurant, name='show_restaurant'),
    path('trending/',views.trending,name='trending'),
    path('add_review/<slug:restaurant_name_slug>/', views.add_review, name='add_review'),
    path('food_styles/', views.food_styles, name='food_styles'),
    path('categories/<str:cuisineName>/', views.categories, name='categories'),
]
