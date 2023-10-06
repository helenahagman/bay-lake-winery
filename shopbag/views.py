from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_shopbag(request):
    """ A view to render the shopping bag contents page """

    return render(request, 'shopbag/shopbag.html')


def add_to_shopbag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        shopbag = request.session.get('shopbag', {})

    if size:
        if item_id in list(shopbag.keys()):
            if size in shopbag[item_id]['items_by_size'].keys():
                shopbag[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated size {size.upper()} '
                                  f'{product.name} quantity to '
                                  f'{shopbag[item_id]["items_by_size"][size]}'))
            else:
                shopbag[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 (f'Added size {size.upper()} '
                                  f'{product.name} to your shopping bag'))
        else:
            shopbag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             (f'Added size {size.upper()} '
                              f'{product.name} to your shopping bag'))
    else:
        if item_id in list(shopbag.keys()):
            shopbag[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {shopbag[item_id]}'))
        else:
            shopbag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your shopping bag')

    request.session['shopbag'] = shopbag
    return redirect(redirect_url)


def adjust_shopbag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopbag = request.session.get('shopbag', {})

    if size:
        if quantity > 0:
            shopbag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{product.name} quantity to '
                              f'{shopbag[item_id]["items_by_size"][size]}'))
        else:
            del shopbag[item_id]['items_by_size'][size]
            if not shopbag[item_id]['items_by_size']:
                shopbag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your shopping bag'))
    else:
        if quantity > 0:
            shopbag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {shopbag[item_id]}'))
        else:
            shopbag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your shopping bag'))

    request.session['shopbag'] = shopbag
    return redirect(reverse('view_shopbag'))


def remove_from_shopbag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shopbag = request.session.get('shopbag', {})

        if size:
            del shopbag[item_id]['items_by_size'][size]
            if not shopbag[item_id]['items_by_size']:
                shopbag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your shopping bag'))
        else:
            shopbag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping bag')

        request.session['shopbag'] = shopbag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
