from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from django_countries.fields import CountryField

from products.models import Product


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return (
            self.user.username
            if self.user else "UserProfile without user"
        )


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        Wishlist.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Wishlist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ManyToManyField(Product, blank=True)

    objects = models.Manager()

    def __str__(self):
        return (
            f'Wishlist for {self.user.username}'
            if self.user and hasattr(self.user, 'username')
            else 'Wishlist without user'
        )


class SiteRecommendation(models.Model):
    """
    User recommendations
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Recommendation by {self.user.username} on {self.created_at}"
