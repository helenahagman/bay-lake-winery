from django.urls import path
from . import views
from .views import wishlist, add_to_wishlist, remove_from_wishlist
from .views import profile_with_recommendation

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>/',
         views.order_history, name='order_history'),
    path('', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/',
         add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/',
         remove_from_wishlist, name='remove_from_wishlist'),
    path('profile_with_recommendation/', views.profile_with_recommendation,
         name='profile_with_recommendation'),
]
