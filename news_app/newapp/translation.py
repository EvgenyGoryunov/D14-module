from modeltranslation.translator import register, TranslationOptions

from .models import *


# импортируем декоратор для перевода и класс настроек, от которого будем наследоваться


# регистрируем наши модели для перевода

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(Category)
class PostTranslationOptions(TranslationOptions):
    fields = ('name',)
