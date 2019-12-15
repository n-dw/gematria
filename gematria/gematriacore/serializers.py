from django.contrib.auth.models import Group
from gematria.users.models import User
from .models import Alphabet, Word, WordValue, WordMeaning, Letter, LetterMeaning, Language, GematriaMethod, GematriaMethodLetterRule

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['uuid', 'title']

class LetterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Letter
        fields = ['id', 'character', 'title', 'letter_order']


class GematriaMethodLetterRuleSerializer(serializers.ModelSerializer):
    letter = LetterSerializer(read_only=True)

    class Meta:
        model = GematriaMethodLetterRule
        fields = ['id', 'numerical_value', 'letter', 'gematria_method']

class AlphabetSerializer(serializers.ModelSerializer):

    letter_set = LetterSerializer(many=True, read_only=True)

    class Meta:
        model = Alphabet
        fields = ['title', 'language', 'letter_set']


class GematriaMethodSerializer(serializers.ModelSerializer):
    gematriamethodletterrule_set = GematriaMethodLetterRuleSerializer(many=True, read_only=True)#serializers.StringRelatedField()

    class Meta:
        model = GematriaMethod
        fields = ['id', 'title', 'language', 'gematriamethodletterrule_set']

class WordValueSerializer(serializers.ModelSerializer):

    #word = serializers.StringRelatedField(many=True)

    class Meta:
        model = WordValue
        fields = ['word', 'value', 'gematria_method']

class WordMeaningSerializer(serializers.ModelSerializer):

    #word = serializers.StringRelatedField(many=True)

    class Meta:
        model = WordMeaning
        fields = ['word', 'meaning']


class WordSerializer(serializers.ModelSerializer):

    wordvalue_set = WordValueSerializer(many=True, read_only=True)
    wordmeaning_set = WordMeaningSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Word.objects.create(**validated_data)
    
    class Meta:
        model = Word
        fields = ['id', 'name_english', 'name_original_language', 'language', 'wordvalue_set', 'wordmeaning_set']





