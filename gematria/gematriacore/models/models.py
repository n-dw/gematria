from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField
from ..managers import(
    WordManager,
    WordValueSuggestionManager,
)
from gematria.users.models import User

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


class Alphabet(TimeStampedModel):
    title = models.CharField(max_length=200)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{0} - Lang: {1}'.format(self.title, self.language)


class GematriaMethod(TimeStampedModel):
    title = models.CharField(max_length=200)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)
    alphabet = models.ForeignKey('Alphabet', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class GematriaMethodLetterRule(TimeStampedModel):
    letter = models.ForeignKey('Letter', on_delete=models.SET_NULL, null=True, blank=True)
    numerical_value = models.FloatField()
    gematria_method = models.ForeignKey('GematriaMethod', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0} - Method: {1}'.format(self.letter, self.gematria_method)

class Language(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Letter(TimeStampedModel):
    title = models.CharField(max_length=200)
    character = models.CharField(max_length=1)
    meanings = models.ManyToManyField('LetterMeaning', blank=True)
    alphabet = models.ForeignKey('Alphabet', on_delete=models.SET_NULL, null=True, blank=True)
    letter_order = models.IntegerField(null=True, blank=True,
                                       help_text='The order from position 1 that this character appears in the alphabet.')

    class Meta:
        ordering = ['letter_order', 'title', 'alphabet']

    def __str__(self):
        return '{0}: {1} {2}'.format(self.title, self.character, self.alphabet)


class LetterMeaning(TimeStampedModel):
    """
       A class that holds the letter meaning for example: Aleph is ox, Beth is House
       """
    meaning = models.CharField(max_length=200)
    is_active = models.NullBooleanField(null=True, blank=True, default=False)

    class Meta:
        ordering = ['meaning']

    def __str__(self):
        return '{0} - Active: {1}'.format(self.meaning, self.is_active)


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


class WordValue(TimeStampedModel):
    value = models.FloatField(blank=True, null=True,)
    word = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE)
    gematria_method = models.ForeignKey('GematriaMethod', blank=True, null=True, on_delete=models.CASCADE)

    objects = models.Manager()
    suggestion_objects = WordValueSuggestionManager()

    def __str__(self):
        return '{0} - {1} : {2}'.format(self.word, self.value, self.gematria_method)

class Word(TimeStampedModel):
    #creator = models.ForeignKey('User', related_name='words', on_delete=models.CASCADE)
    name_english = models.CharField(max_length=200)
    name_original_language = models.CharField(max_length=200)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)
    characters_alpha = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):

        no_spaces_original_name = "".join(self.name_original_language.split())

        self.characters_alpha = ''.join(sorted(no_spaces_original_name))

        super(Word, self).save(*args, **kwargs)  # Call the "real" save() method.

        #if we have gematria methods calculate the values
        num_gem_methods = GematriaMethod.objects.filter(language=self.language).count()

        if num_gem_methods:
            gem_methods = GematriaMethod.objects.filter(language=self.language)

            for cipher in gem_methods:

                gematria_value = 0

                for character in no_spaces_original_name:
                    # get the letter object
                    letter = Letter.objects.get(character=character)
                    # get the gematria letter rule so we can find the numerical value for the letter
                    glr = GematriaMethodLetterRule.objects.get(letter=letter, gematria_method=cipher)
                    gematria_value = gematria_value + glr.numerical_value


                obj, created = WordValue.objects.update_or_create(word=self, value=gematria_value, gematria_method=cipher)



    def __str__(self):
        return '{0} - {1} : {2}'.format(self.name_english, self.name_original_language, self.language)


class WordMeaning(TimeStampedModel):
    """
       A class that holds the letters English equivalent i.e Beth = B,V
       """
    meaning = models.CharField(max_length=200)
    word = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE)
    source = models.TextField(blank=True, null=True, help_text='citation')
    is_active = models.NullBooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return '{0} - {1}'.format(self.word, self.meaning)



