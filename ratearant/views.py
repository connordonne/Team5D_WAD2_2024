from django.shortcuts import render


# Create your views here.


def home(request):
    context_dict = {'message': 'Placeholder for the Team 5D Rate-A-Rant homepage',
                    'isHomePage': True}
    return render(request, 'ratearant/home.html', context=context_dict)


def about(request):
    context_dict = {'message': 'Placeholder for the Team 5D Rate-A-Rant About page'}
    return render(request, 'ratearant/about.html', context=context_dict)


def register(request):
    context_dict = {'message': 'Placeholder for the Team 5D Rate-A-Rant Register page'}
    return render(request, 'ratearant/register.html', context=context_dict)

def login(request):
    context_dict = {'message': 'Placeholder for the Team 5D Rate-A-Rant Login page'}
    return render(request, 'ratearant/login.html', context=context_dict)