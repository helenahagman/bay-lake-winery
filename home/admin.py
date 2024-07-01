from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ("name", "email", "date_posted")
    search_fields = ["name"]

# @admin.register(SiteRecommendation)
# class SiteRecommendationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'recommendation_text', 'created_at')
#     list_filter = ('created_at', 'user')
#     search_fields = ('user__username', 'recommendation_text')