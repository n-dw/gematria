from django.contrib import admin
from django.utils.html import format_html

from gematria.gematriacore.models import(
    LetterPower,
    LetterMeaning,
    Letter,
    WordMeaning,
    Word,
    WordValue,
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

admin.site.register(WordMeaning)
class WordMeaningAdminInline(admin.TabularInline):
    model = WordMeaning

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    search_fields = ['name_english', 'name_original_language']
    inlines = (WordMeaningAdminInline,)

@admin.register(WordValue)
class WordValueAdmin(admin.ModelAdmin):
    pass

@admin.register(LetterMeaning)
class LetterMeaningAdmin(admin.ModelAdmin):
    pass

admin.site.register(LetterPower)
class LetterPowerAdminInline(admin.TabularInline):
    model = LetterPower

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    filter_horizontal = ('meanings',)
    search_fields = ['title', 'character']
    list_display = ['title', 'char_span', 'letter_order','alphabet']
    list_filter = ['alphabet']


    def char_span(self, instance):
        return format_html("""<span class="u-lang-hebrew">{0}</a>""", instance.character)

    char_span.short_description = 'Character'

admin.site.register(GematriaMethodLetterRule)
class GematriaMethodLetterRuleAdminInline(admin.TabularInline):
    model = GematriaMethodLetterRule

@admin.register(GematriaMethod)
class GematriaMethodAdmin(admin.ModelAdmin):
    inlines = (GematriaMethodLetterRuleAdminInline,)
