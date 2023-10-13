from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:product_id>/',
         views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/delete/<int:product_id>/',
         views.delete_product, name='delete_product'),
    path('products/edit/<int:product_id>/',
         views.edit_product, name='edit_product'),
    path('render-quantity-input-script/', views.render_quantity_input_script,
         name='render_quantity_input_script'),
]
