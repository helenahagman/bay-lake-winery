from django.shortcuts import render
# from django.views import generic


def index_view(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
