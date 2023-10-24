from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from shopbag.contexts import shopbag_contents

import stripe


def checkout_view(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    shopbag = request.session.get('shopbag', {})
    if not shopbag:
        messages.error(request, 'Your bag is empty')
        return redirect(reverse('products'))

    current_shopbag = shopbag_contents(request)
    total = current_shopbag['total']
    stripe_total = round(total * 100)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # Get the client_secret from the PaymentIntent object
    client_secret = intent.client_secret

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, template, context)


def checkout_success(request):
    pass


def cache_checkout_data(request):
    pass
