from django.shortcuts import render
# from django.views import generic


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
