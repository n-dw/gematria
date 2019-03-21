from django.contrib import admin
from django.utils.html import format_html

from gematria.gematriacore.models import(
    LetterPower,
    LetterMeaning,
    Letter,
    WordMeaning,
    Word,
    Dictionary,
    Alphabet,
    Language,
    GematriaMethodLetterRule,
    GematriaMethod
)
# Register your models here.
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Alphabet)
class AlphabetAdmin(admin.ModelAdmin):
    pass

@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    pass

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass

@admin.register(WordMeaning)
class WordMeaningAdmin(admin.ModelAdmin):
    pass

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    filter_horizontal = ('powers', 'meanings')
    search_fields = ['title', 'character']
    list_display = ['title', 'char_span', 'alphabet']
    list_filter = ['alphabet']

    def char_span(self, instance):
        return format_html("""<span class="u-lang-hebrew">{0}</a>""", instance.character)

    char_span.short_description = 'Character'

@admin.register(LetterMeaning)
class LetterMeaningAdmin(admin.ModelAdmin):
    pass

@admin.register(LetterPower)
class LetterPowerAdmin(admin.ModelAdmin):
    pass

@admin.register(GematriaMethod)
class GematriaMethodAdmin(admin.ModelAdmin):
    pass

@admin.register(GematriaMethodLetterRule)
class GematriaMethodLetterRuleAdmin(admin.ModelAdmin):
    pass
