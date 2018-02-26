from django.shortcuts import render

# Create your views here.


def images(request):
    '''
    function to display the index page
    '''
    return render(request, 'images.html')


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
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Article.search_by_order(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
