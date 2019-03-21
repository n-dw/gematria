from django.contrib import admin
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
    list_display = ['title', 'character', 'alphabet']
    list_filter = ['alphabet']

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
