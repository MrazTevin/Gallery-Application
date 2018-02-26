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

    return render(request, 'home.html')


def search_results(request):
    '''
    search function to display search search_results
    args:
    order defines category
    '''
    if 'order' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_order(search_term)
        message = f"{seach_term}"

        return render(request, 'search.html', {"message": message,
                                               "photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return_render(request, 'search.html', {"message": message})
