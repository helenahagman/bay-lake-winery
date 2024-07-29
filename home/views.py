from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from .forms import ContactForm
from profiles.models import SiteRecommendation


def index_view(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about_view(request):
    """ A view to the about page """
    recommendations = SiteRecommendation.objects.all()[:5]
    context = {
        'recommendations': recommendations,
    }
    return render(request, 'home/about.html', context)


def contact_us_view(request):
    """
    View to return the Contact form
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.save()

            messages.success(
                request,
                "Your message has been sent. We will contact you shortly.",
            )
            return about_view(request)
        else:
            messages.error(
                request, "Form submission failed. Please check and try again."
            )
    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "home/contact_us.html", context)
