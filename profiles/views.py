from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model
from django.http import JsonResponse

from .models import UserProfile, Wishlist, SiteRecommendation
from .forms import UserProfileForm, RecommendationForm

from checkout.models import Order
from products.models import Product

from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

UserModel = get_user_model()

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
    print(recommendations)
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


def signup_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.email = form.cleaned_data.get('email')
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = UserProfileForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('profile')
    else:
        return render(request, 'account_activation_invalid.html')
