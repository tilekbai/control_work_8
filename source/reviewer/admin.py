from django.contrib import admin
from .models import Good
# Register your models here.

class GoodAdmin(admin.ModelAdmin):
    list_display = ["id", "summary", "description", "category", "picture"]
    list_filter = ["id", "summary", "category"]
    search_fields = ["description", "summary", "category"]
    fields = ["id", "summary", "description", "category", "picture"]
    readonly_fields = ["id"]

admin.site.register(Good, GoodAdmin)