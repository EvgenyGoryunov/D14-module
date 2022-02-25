from django.contrib import admin


# переопределение стандартных админ-инструментов)
from modeltranslation.admin import TranslationAdmin

from .models import *


def like_plus_five(modeladmin, request, queryset):
    # функция накрутки лайков статье
    for posts in queryset:
        posts.rating = posts.rating + 5
        posts.save()


def like_minus_five(modeladmin, request, queryset):
    # функция  скрутки лайков статье
    for posts in queryset:
        posts.rating = posts.rating - 5
        posts.save()


# class PostAdmin(TranslationAdmin):
#     model = Post


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'category', 'author', 'rating',)
#     list_filter = ('category', 'author')
#     actions = [like_plus_five, like_minus_five]  # добавляем действия в список
#     search_fields = ('title',)  # тут всё очень похоже на фильтры из запросов в базу
    # model = Post


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name',)

class PostAdmin(TranslationAdmin):
    model = Post

class CategoryAdmin(TranslationAdmin):
    model = Category


admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
