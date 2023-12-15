from django.urls import path
from . import views
from .views import contact_us_view


urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path("contact/", contact_us_view, name="contact_us"),
]
