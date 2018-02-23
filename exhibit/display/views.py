from django.shortcuts import render

# Create your views here.


def welcome(request):
    '''
    function to display the index page
    '''
    return render(request, 'welcome.html')


def home(request):
    '''
    home function to display home images
    '''

    return render(request, 'all-display/home.html')
