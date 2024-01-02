from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User


# code from walk through project
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = CloudinaryField('image', default='default_cloudinary_url')

    cloudinary_image_url = models.URLField(max_length=2000, null=True, blank=True)

    objects = models.Manager()

    is_in_wishlist = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f'Wishlist for {self.user.username}'
