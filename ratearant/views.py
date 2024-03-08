from django.shortcuts import render

# User login and logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from ratearant.forms import UserForm
from ratearant.models import Restaurant


# Create your views here.


def home(request):
    restaurant_list = Restaurant.objects.order_by('name')[:5]
    fave_restaurant_list = Restaurant.objects.order_by('name')[5:]

    context_dict = {'top_message': "Top Rated Restaurants", 'fave_message': "Favourite Restaurants",
                    'restaurants': restaurant_list, 'fave_restaurants': fave_restaurant_list}
    return render(request, 'ratearant/home.html', context=context_dict)


def about(request):
    context_dict = {'message': 'Placeholder for the Team 5D Rate-A-Rant About page',
                    'isAboutPage': True}
    return render(request, 'ratearant/about.html', context=context_dict)


def show_restaurant(request, restaurant_name_slug):
    context_dict = {}

    try:
        # getting the restaurant reocrds by the slug
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
        context_dict = {'restaurant': restaurant, 'name': restaurant.name,
                        'address': restaurant.address,
                        'phone': restaurant.phone,
                        'website': restaurant.website,
                        'openingTime': restaurant.openingTime,
                        'priceRange': restaurant.priceRange,
                        'cuisine': restaurant.cuisine}

    except Restaurant.DoesNotExist:
        context_dict['restaurant'] = None
        context_dict['name'] = None
        context_dict['address'] = None
        context_dict['phone'] = None
        context_dict['website'] = None
        context_dict['openingTime'] = None
        context_dict['priceRange'] = None
        context_dict['cuisine'] = None

    return render(request, 'ratearant/restaurant.html', context=context_dict)


# User login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('ratearant:home'))
            else:
                return HttpResponse("Your user account is disabled.")
    else:
        return render(request, 'ratearant/login.html')


# User logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('ratearant:home')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()
    return render(request,
                  'ratearant/register.html',
                  context={'user_form': user_form,
                           'registered': registered})


# User delete
"""
@login_required
def delete_account(request):
    user = get_user_model().objects.get(username=request.user.username)
    user.delete()
    return redirect('ratearant:home')
"""
