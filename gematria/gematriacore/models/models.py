from django.db import models
from ..managers import(
    WordManager,
)

# Create your models here.

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class LetterPower(TimeStampedModel):
    """
       A class that holds the letters English equivalent i.e Beth = B,V
       """
    power = models.CharField(max_length=20)
    letter = models.ForeignKey('Letter', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.NullBooleanField(null=True, blank=True, default=False)

    class Meta:
        ordering = ['power', 'letter']

    def __str__(self):
        return '{0} - {1} Active: {2}'.format(self.power, self.letter, self.is_active)

class LetterMeaning(TimeStampedModel):
    """
       A class that holds the letters English equivalent i.e Beth = B,V
       """
    meaning = models.CharField(max_length=200)
    is_active = models.NullBooleanField(null=True, blank=True, default=False)

    class Meta:
        ordering = ['meaning']

    def __str__(self):
        return '{0} - Active: {1}'.format(self.meaning, self.is_active)

class Letter(TimeStampedModel):
    title = models.CharField(max_length=200)
    character = models.CharField(max_length=1)
    meanings = models.ManyToManyField('LetterMeaning', blank=True)
    alphabet = models.ForeignKey('Alphabet', on_delete=models.SET_NULL, null=True, blank=True)
    letter_order = models.IntegerField(null=True, blank=True, max_length=4)

    class Meta:
        ordering = ['letter_order', 'title', 'alphabet']

    def __str__(self):
        return '{0}: {1} {2}'.format(self.title, self.character, self.alphabet)

class WordMeaning(TimeStampedModel):
    """
       A class that holds the letters English equivalent i.e Beth = B,V
       """
    meaning = models.CharField(max_length=200)
    word = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE)
    is_active = models.NullBooleanField(null=True, blank=True, default=False)

class Word(TimeStampedModel):
    name_english = models.CharField(max_length=200)
    name_original_language = models.CharField(max_length=200)
    letters = models.ManyToManyField('Letter', blank=True)

    related = WordManager()

    def __str__(self):
        return '{0} - {1}'.format(self.name_english, self.name_original_language)

class Dictionary(TimeStampedModel):
    title = models.CharField(max_length=200)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)
    words = models.ManyToManyField('Word', blank=True)
    is_base_dict = models.NullBooleanField(default=False)

class Alphabet(TimeStampedModel):
    title = models.CharField(max_length=200)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{0} - Lang: {1}'.format(self.title, self.language)

class Language(TimeStampedModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class GematriaMethodLetterRule(TimeStampedModel):
    letter = models.ForeignKey('Letter', on_delete=models.SET_NULL, null=True, blank=True)
    numerical_value = models.FloatField()
    gematria_method = models.ForeignKey('GematriaMethod', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0} - Method: {1}'.format(self.letter, self.gematria_method)

class GematriaMethod(TimeStampedModel):
    title = models.CharField(max_length=200)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)
    alphabet = models.ForeignKey('Alphabet', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


