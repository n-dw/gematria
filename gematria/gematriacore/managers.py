from django.db import models

class WordManager(models.Manager):
    def get_queryset(self):
        return super().get_query_set().filter()


class DocumentQuerySet(models.QuerySet):
    def pdfs(self):
        return self.filter(file_type='pdf')

    def smaller_than(self, size):
        return self.filter(size__lt=size)

class WordValueSuggestionManager(models.Manager):
    def get_queryset(self):
        objects     = super().get_query_set().filter()

        filtered_values = {}

        for obj in objects:
            filtered_values[obj.value] = obj

        return filtered_values
