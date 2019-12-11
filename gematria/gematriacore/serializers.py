from django.contrib.auth.models import Group
from gematria.users.models import User
from .models import Word, WordValue, Language

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class WordSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Word.objects.create(**validated_data)
    
    class Meta:
        model = Word
        fields = ['id', 'name_english', 'name_original_language', 'language']

class WordValueSerializer(serializers.ModelSerializer):

    word = WordSerializer()

    class Meta:
        model = WordValue
        fields = ['word', 'value', 'gematria_method']

class WordMeaningSerializer(serializers.ModelSerializer):

    word = WordSerializer()

    class Meta:
        model = WordValue
        fields = ['word', 'meaning', 'gematria_method']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['uuid', 'title']


