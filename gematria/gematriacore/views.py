# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView, UpdateView, ListView
from django.urls import reverse
from django.db.models import Q

from .models import *
from gematria.users.models import User

from django.views.generic import TemplateView

from django.contrib.auth.models import Group

from .serializers import *

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework import filters

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'groups': reverse('groups-list', request=request, format=format),
        'words': reverse('word-list', request=request, format=format)
    })

class SuggestionsView(APIView):
    # {
    #     id:
    #     object_type:
    #     value:
    #     input_value:
    # }
    def get(self, request, format=None):
        query_string = request.query_params['search']

        if query_string.isnumeric():
            word_values = WordValue.objects.filter(value__contains=query_string).order_by('value').distinct('value').all()
            wordValueSerializer = WordValueSerializer(word_values, many=True)

            suggestions = []
            for word_val in word_values:
                suggestion = {
                    'id': word_val.id,
                    'type': 'number' ,
                    'value': word_val.value,
                    'search_value': word_val.value ,
                }

                suggestions.append(suggestion)

            return Response(suggestions)

        words_english = Word.objects.filter(name_english__icontains=query_string).all()
        words_original = Word.objects.filter(name_original_language__icontains=query_string).all()

        words = []

        search_value = 'name_english'

        if words_english.count() > 0:
            words = words_english
            search_value = 'name_english'

        if words_original.count() > 0:
            words = words_original
            search_value = 'name_original_language'

        eng_count = words_english.count()

        wordSerializer = WordSerializer(words, many=True)

        suggestions = []
        for word in words:
            suggestion = {
                'id': word.id,
                'type': 'word',
                'value': word.name_english + ' : ' + word.name_original_language,
                'search_value': getattr(word, search_value),
            }

            suggestions.append(suggestion)

        return Response(suggestions)

class WordNumericalValue(generics.GenericAPIView):
    queryset = Word.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        word = self.get_object()
        word_values = WordValue.objects.filter(word=word).all()
        num_values = {}

        for word_value in word_values:
            num_values[word_value.gematria_method.title.lower()] = word_value.value

        return Response(num_values)


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'uuid']


class WordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Word.objects.order_by('language', 'wordvalue__value').all()
    serializer_class = WordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_english', 'name_original_language']
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WordValueViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = WordValue.objects.all()
    serializer_class = WordValueSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['value', 'word']

# class WordList(generics.ListCreateAPIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer
#
# class WordDetail(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'uuid']

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



class HomeView(TemplateView):
    template_name = "pages/home.html"

#WORDS
class WordListView(ListView):
    model = Word

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Each Word add in it's meanings and values
        # word = {
        #     'word': Word,
        #     'meanings': [WordMeaning]
        # }

        words = []

        for word in context['object_list'].filter():

            word_meanings = WordMeaning.objects.filter(word=word)

            new_word = {
                'word': word,
                'meanings': word_meanings
            }

            words.append(new_word)

        context['words'] = words
        return context
