from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_shopbag(request):
    """ A view to render the shopping bag contents page """
    return render(request, 'shopbag/shopbag.html')


def add_to_shopbag(request, item_id):
    """ Add a specified number of a product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    shopbag = request.session.get('shopbag', {})
    if item_id in shopbag:
        shopbag[item_id] += quantity
        success_message = (
            f'Updated {product.name} quantity to '
            f'{shopbag[item_id]}'
        )
    else:
        shopbag[item_id] = quantity
        success_message = f'Added {product.name} to shopping bag'

    messages.success(request, success_message)
    request.session['shopbag'] = shopbag
    return redirect(redirect_url)


def adjust_shopbag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    shopbag = request.session.get('shopbag', {})
    if item_id in shopbag:
        if quantity > 0:
            shopbag[item_id] = quantity
            success_message = (
                f'Updated {product.name} quantity to '
                f'{shopbag[item_id]}'
            )
        else:
            shopbag.pop(item_id)
            success_message = f'Removed {product.name} from the shopping bag'

        messages.success(request, success_message)

    request.session['shopbag'] = shopbag
    return redirect(reverse('view_shopbag'))


def remove_from_shopbag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        shopbag = request.session.get('shopbag', {})

        if item_id in shopbag:
            shopbag.pop(item_id)
            success_message = f'Removed {product.name} from your shopping bag'
            messages.success(request, success_message)

        request.session['shopbag'] = shopbag
        return HttpResponse(status=200)

    except Exception as e:
        error_message = f'Error removing item: {e}'
        messages.error(request, error_message)
        return HttpResponse(status=500)

