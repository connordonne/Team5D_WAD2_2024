from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context_dict = {'message': 'Placeholder for the Team 5D Ratearant homepage'}
    return render(request, 'ratearant/index.html', context=context_dict)
