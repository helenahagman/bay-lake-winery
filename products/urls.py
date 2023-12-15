from django.urls import path
from . import views
from .views import wishlist, add_to_wishlist, remove_from_wishlist


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product, name='delete_product'),
    path('wishlist/', wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/',
         add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/',
         remove_from_wishlist, name='remove_from_wishlist'),
]
