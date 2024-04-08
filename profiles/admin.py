from django.contrib import admin
from .models import Wishlist, SiteRecommendation, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'default_phone_number', 'default_street_address1', 
        'default_street_address2', 'default_town_or_city', 
        'default_county', 'default_postcode', 'default_country'
    )
    list_filter = ('user', 'default_country',)
    search_fields = (
        'user__username', 'default_phone_number', 'default_street_address1', 
        'default_street_address2', 'default_town_or_city', 
        'default_county', 'default_postcode'
    )

    def __str__(self):
        return (
            self.user.username
            if self.user else "UserProfile without user"
        )

admin.site.register(Wishlist)
admin.site.register(SiteRecommendation)
