from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
import logging

from products.models import Product

logger = logging.getLogger(__name__)

def view_shopbag(request):
    """ A view to render the shopping bag contents page """
    return render(request, 'shopbag/shopbag.html')


def add_to_shopbag(request, item_id):
    """ Add a specified number of a product to the shopping bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        
        if quantity > 0:
            shopbag = request.session.get('shopbag', {})
            shopbag[item_id] = shopbag.get(item_id, 0) + quantity
            request.session['shopbag'] = shopbag

            success_message = f'Added {product.name} to your shopping bag'
            messages.success(request, success_message)
        else:
            messages.error(request, 'Wrong amount')
    
    except Exception as e:
        error_message = f'Error adding item: {e}'
        logger.error(error_message)
        messages.error(request, error_message)

    print(request.session['shopbag'])
    return redirect(redirect_url)


def adjust_shopbag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))

    
        if quantity > 0:
            shopbag = request.session.get('shopbag', {})
            shopbag[item_id] = quantity
            request.session['shopbag'] = shopbag

            success_message = f'Updated {product.name} quantity to {quantity}'
        else:
            shopbag.pop(item_id, None)
            success_message = f'Removed {product.name} from the shopping bag'
            messages.success(request, success_message)

    except Exception as e:
        error_message = f'Error adjusting item: {e}'
        logger.error(error_message)
        messages.error(request, error_message)

    return redirect(reverse('view_shopbag'))


def remove_from_shopbag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        shopbag = request.session.get('shopbag', {})
        shopbag.pop(item_id, None)
        request.session['shopbag'] = shopbag

        success_message = f'Removed {product.name} from shopping bag'
        messages.success(request, success_message)
        
    except Exception as e:
        error_message = f'Error removing item: {e}'
        messages.error(request, error_message)
        return HttpResponse(status=500)
    
    return redirect(reverse('view_shopbag'))
