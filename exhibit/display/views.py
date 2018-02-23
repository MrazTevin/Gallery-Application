from django.shortcuts import render

# Create your views here.


def welcome(request):
    '''
    view function for welcome
    '''
    return render(request, 'welcome.html')


def home(request):
    '''
    home function to display home images
    '''

    return HttpResponse('View home images for free')
