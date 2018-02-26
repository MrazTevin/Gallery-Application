from django.shortcuts import render
from .models import Image
# Create your views here.


def images(request):
    '''
    function to display the index page
    '''
    images = Image.objects.all()
    return render(request, 'images.html', {"images": images})


def home(request):
    '''
    home function to display home images
    '''

    return render(request, 'home.html')


def search_results(request):
    '''
    search function to display search search_results
    args:
    order defines category
    '''
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
