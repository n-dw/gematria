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
    letter_order = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['letter_order', 'title', 'alphabet']

    def __str__(self):
        return '{0}: {1} {2}'.format(self.title, self.character, self.alphabet)

class WordValue(TimeStampedModel):
    value = models.FloatField()
    word = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE)
    gematria_method = models.ForeignKey('GematriaMethod', blank=True, null=True, on_delete=models.CASCADE)

class WordMeaning(TimeStampedModel):
    """
       A class that holds the letters English equivalent i.e Beth = B,V
       """
    meaning = models.CharField(max_length=200)
    word = models.ForeignKey('Word', blank=True, null=True, on_delete=models.CASCADE)
    is_active = models.NullBooleanField(null=True, blank=True, default=False)


class WordSpelling(TimeStampedModel):
    """
          The Letter and the Position in the word of that letter
           """
    letter = models.ForeignKey('letter', on_delete=models.CASCADE, null=True, blank=True)
    position = models.PositiveSmallIntegerField()
    word = models.ForeignKey('Word', related_name='spelling', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}, pos: {1}, {2}'.format(self.letter, self.position, self.word)

class Word(TimeStampedModel):
    name_english = models.CharField(max_length=200)
    name_original_language = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.

        #create the spelling of each word it's important to break the letters up
        word_len = len(self.name_original_language)
        for idx in range(word_len):
            letter = Letter.objects.get(character=self.name_original_language[idx])

            if letter:
                position = word_len - idx
                obj, created = WordSpelling.objects.update_or_create(
                    letter=letter, position=position, word=self
                )


        #if we have gematria methods calculate the values
        num_gem_methods = GematriaMethod.objects.count()
        if num_gem_methods:
            gem_methods = GematriaMethod.objects.all()

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


