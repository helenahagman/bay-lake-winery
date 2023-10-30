from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.http import JsonResponse


def index_view(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about_view(request):
    """ A view to the about page """
    return render(request, 'home/about.html')


def contact_us_view(request):
    """
    View to return the Contact form
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your message has been sent. We will contact you shortly.",
            )
            return redirect("contact")
        else:
            messages.error(
                request, "Form submission failed. Please check and try again."
            )
    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "home/about.html", context)
