# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView, UpdateView, ListView
from django.urls import reverse
from .models import *

from django.views.generic import TemplateView

from django.contrib.auth.models import Group

from rest_framework import viewsets
from .serializers import *
from rest_framework import generics


class WordList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """

    queryset = Word.objects.all()
    serializer_class = WordSerializer

class WordDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Word.objects.all()
    serializer_class = WordSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


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
