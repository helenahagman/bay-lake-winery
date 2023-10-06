from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopbag, name='view_shopbag'),
    path('add/<item_id>/', views.add_to_shopbag, name='add_to_shopbag'),
    path('adjust/<item_id>/', views.adjust_shopbag, name='adjust_shopbag'),
    path('remove/<item_id>/', views.remove_from_shopbag, name='remove_from_shopbag'),
]
