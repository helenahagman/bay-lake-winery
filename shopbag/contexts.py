from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def shopbag_contents(request):

    shopbag_items = []
    total = 0
    product_count = 0
    shopbag = request.session.get('shopbag', {})

    for item_id, quantity in shopbag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += quantity
        shopbag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })
        
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'shopbag_items': shopbag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
