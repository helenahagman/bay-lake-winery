from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm

import cloudinary.uploader


def all_products(request):
    """ A view to return the product page """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, ("Oops, forgot to enter a search criteria?"))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    product_list = []
    for product in products:
        if product.cloudinary_image_url:
            image_url = product.cloudinary_image_url
        elif product.image:
            upload_image = cloudinary.uploader.upload(product.image)
            image_url = uploaded_image['secure_url']
            product.cloudinary_image_url = image_url
            product.save()
        else:
            image_url = ''
        
        product_list.append({
            'product': product,
            'image_url': image_url,

        })

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': f'{sort}_{direction}',
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return the product details  """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'cloudinary_image_url': cloudinary_image_url,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a new product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, ('No product added'))
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ Edit an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Handle Cloudinary image upload
            image = form.cleaned_data.get('image')
            if image:
                uploaded_image = cloudinary.uploader.upload(image)
                # Set Cloudinary URL to the product instance
                product.image_url = uploaded_image['secure_url']

            form.save()
            messages.success(request, 'Product updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, ('No product updated'))
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
        'cloudinary_image_url': cloudinary_image_url,
    }
    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ Delete a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product removed')
    return redirect(reverse('products'))


def render_quantity_input_script(request):
    """ A view to render the quantity input script template """
    return render(request, 'products/includes/quantity_input_script.html')
