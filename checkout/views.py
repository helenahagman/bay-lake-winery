from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from shopbag.contexts import shopbag_contents 


def checkout_view(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your bag is empty')
        return redirect(reverse('products'))

    current_shopbag = shopbag_contents(request)
    total = current_shopbag['total']
    stripe_total = round(total * 100)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O4fn8ISFE7U70bBbKXW3bjI23jy4FQOAAgEUKF5BdQ9bEoBu6LfEIuA0SduI4vvPvMuZlmmcDCJhkPRjZuvMGaf003jmx6ZpY',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


def checkout_success(request):
    pass


def cache_checkout_data(request):
    pass
