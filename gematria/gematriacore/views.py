# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView, UpdateView, ListView
from django.urls import reverse
from .models import *
from gematria.users.models import User

from django.views.generic import TemplateView

from django.contrib.auth.models import Group

from .serializers import *

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from rest_framework import renderers

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'groups': reverse('groups-list', request=request, format=format),
        'words': reverse('word-list', request=request, format=format)
    })


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

class WordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        word = self.get_object()
        return Response(word)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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
