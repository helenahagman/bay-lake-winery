from django.shortcuts import render
from .forms import ContactFormModelForm


def index_view(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about_view(request):
    """ A view to the about page """

    return render(request, 'home/about.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'includes/toasts/toast_thankyou.html', {'message': 'Thank you for your message!'})

    else:
        form = ContactFormModelForm()

    return render(request, '', {'form': form})
