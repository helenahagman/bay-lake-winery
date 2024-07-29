from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model

from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

from .models import UserProfile, Wishlist, SiteRecommendation
from .forms import UserProfileForm, RecommendationForm, CustomUserCreationForm

from checkout.models import Order
from products.models import Product

UserModel = get_user_model()

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        rec_form = RecommendationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            print(form.errors)
            messages.error(request, 'Update failed, ensure the form is valid.')

        if rec_form.is_valid():
            recommendation = rec_form.save(commit=False)
            recommendation.user = request.user
            recommendation.save()
            messages.success(request, 'Thank you for your feedback')
        else:
            print(rec_form.errors)
            messages.error(request, 'Something went wrong, please try again')
    else:
        form = UserProfileForm(instance=profile)
        rec_form = RecommendationForm()

    orders = profile.orders.all()

    try:
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist_products = wishlist.product.all()
    except Wishlist.DoesNotExist:
        wishlist = None
        wishlist_products = []

    recommendations = SiteRecommendation.objects.filter(user=request.user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'rec_form': rec_form,
        'orders': orders,
        'wishlist': wishlist,
        'wishlist_products': wishlist_products,
        'recommendations': recommendations,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
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
        product = get_object_or_404(Product, id=product_id)

        if request.user.is_authenticated:
            user_wishlist, _ = Wishlist.objects.get_or_create(
                user=request.user
                )
            if product in user_wishlist.product.all():
                user_wishlist.product.remove(product)
            else:
                user_wishlist.product.add(product)

        return JsonResponse({'is_in_wishlist': product in user_wishlist.product.all()})

    return JsonResponse({'error': 'Invalid request'})


@login_required
def wishlist(request):
    """ A view to display the user's wishlist """
    user_wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist_products = user_wishlist.product.all()

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
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    if product not in wishlist.product.all():
        wishlist.product.add(product)
        messages.success(request, 'Product added to wishlist')
    else:
        messages.info(request, 'Product already added to wishlist')

    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):
    """ A view to remove a product from the wishlist """
    product = get_object_or_404(Product, id=product_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    if product in wishlist.product.all():
        wishlist.product.remove(product)
        if request.is_ajax():
            return JsonResponse({'success': True, 'product_id': product_id})
        messages.success(request, 'Product removed from wishlist')
    else:
        if request.is_ajax():
            return JsonResponse({'success': False, 'product_id': product_id})
        messages.info(request, 'Product is not in wishlist')

    return redirect('profile')


def about(request):
    recommendations = SiteRecommendation.objects.all()[:5]
    print(recommendations)
    return render(request, 'about.html', {'recommendations': recommendations})


@login_required
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
        {'form': form, 'recommendations': recommendations}
    )



def signup_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = False  # User will be activated after email confirmation
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # Link the user profile with the created user
            profile.save()

            # Send an email for account activation
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, 'Please confirm your email address to complete the registration.')
            return redirect('account_activation_sent')
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserProfileForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'signup.html', context)


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
