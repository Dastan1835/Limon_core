from django.contrib import admin
from journal.models import Publication, Category, Hashtag, AboutMe
# Register your models here.


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ["description"]