from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def welcome(request):
    '''
    view function for welcome
    '''
    return HttpResponse('HelloWorld')


def home(request):
    '''
    home function to display home images
    '''

    return HttpResponse('View home images for free')
