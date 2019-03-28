# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView, UpdateView, ListView
from django.urls import reverse
from .models import *

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

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

#DICTIONARY
class DictionaryDetailView(LoginRequiredMixin, DetailView):
    model = Dictionary

class TasteUpdateView(UpdateView):
    model = Dictionary

    def get_success_url(self):
        return reverse('dictionary:detail',
                       kwargs={'pk': self.object.pk})
