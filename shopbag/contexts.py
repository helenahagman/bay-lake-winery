from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def shopbag_contents(request):

    shopbag_items = []
    total = 0
    product_count = 0
    delivery = 0
    shopbag = request.session.get('shopbag', {})
    
    for item_id, quantity in shopbag.items():
        product = get_object_or_404(Product, pk=item_id)
        item_total = quantity * product.price
        total += item_total
        product_count += quantity
        shopbag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'item_total': item_total,
        })

    delivery_percentage = Decimal(settings.DELIVERY_PERCENTAGE)
    delivery = total * (delivery_percentage / 100)    
        
    grand_total = delivery + total

    context = {
        'shopbag_items': shopbag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
