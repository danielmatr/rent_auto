from django.contrib import admin

# Register your models here.
from main.models import *


class AutoPostImageInline(admin.TabularInline):
    model = AutoPostImage
    max_num = 5
    min_num = 1


@admin.register(AutoPost)
class PostAdmin(admin.ModelAdmin):
    inlines = [AutoPostImageInline, ]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "post", "ip")


admin.site.register(RatingStar)
admin.site.register(Category)
