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
    
    #value = serializers.HyperlinkedIdentityField(view_name='word-value', format='html')
    
    class Meta:
        model = Word
        fields = ['name_english', 'name_original_language', 'language']

class WordValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordValue
        fields = ['word', 'value', 'gematria_method']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['uuid', 'title']


