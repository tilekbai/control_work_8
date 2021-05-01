from django.contrib import admin
from .models import Good, Review
# Register your models here.

class GoodAdmin(admin.ModelAdmin):
    list_display = ["id", "summary", "description", "category", "picture"]
    list_filter = ["id", "summary", "category"]
    search_fields = ["description", "summary", "category"]
    fields = ["id", "summary", "description", "category", "picture"]
    readonly_fields = ["id"]

admin.site.register(Good, GoodAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "review_text", "rating", "good", "moderation", "start_date"]
    list_filter = ["id"]
    search_fields = ["good", "author", "rating"]
    fields = ["id", "author", "review_text", "rating", "good", "moderation"]
    readonly_fields = ["id", "start_date", "update_date"]

admin.site.register(Review, ReviewAdmin)