from . import views
from django.urls import path


urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_us, name='contact_us'),
]
