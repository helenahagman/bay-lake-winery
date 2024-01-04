from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import UserProfile, Wishlist, SiteRecommendation
from .forms import UserProfileForm, RecommendationForm

from checkout.models import Order
from products.models import Product


@login_required()
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed, ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = None

    recommendations = SiteRecommendation.objects.filter(user=request.user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist': wishlist,
        'recommendations': recommendations,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'this is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def toggle_wishlist(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        if request.user.is_authenticated:
            user_wishlist, _ = Wishlist.objects.get_or_create(
                user=request.user)
            if product in user_wishlist.products.all():
                user_wishlist.products.remove(product)
            else:
                user_wishlist.products.add(product)

        return JsonResponse({'is_in_wishlist': product in user_wishlist.products.all()})

    return JsonResponse({'error': 'Invalid request'})


def wishlist(request):
    """ A view to display the user's wishlist """
    user_wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist_products = user_wishlist.products.all()

    template = 'profiles/wishlist.html'
    context = {
        'wishlist': user_wishlist,
        'wishlist_products': wishlist_products,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add a product to the wishlist """
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.success(request, 'Product added to wishlist')
    else:
        messages.info(request, 'Product already added to wishlist')

    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):
    """ A view to remove a product from the wishlist """
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, 'Product removed from wishlist')
    else:
        messages.info(request, 'Product is not in wishlist')

    return redirect('product_detail', product_id=product_id)


def about(request):
    recommendations = SiteRecommendation.objects.all()[:5]
    return render(request, 'about.html', {'recommendations': recommendations})


@login_required()
def profile_with_recommendation(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.save()
            messages.success(request, 'Recommendation added')

    else:
        form = RecommendationForm()

    recommendations = SiteRecommendation.objects.filter(user=request.user)

    return render(
        request, 'profiles/profile.html',
        {'form': form, 'recommendation': recommendations}
    )
