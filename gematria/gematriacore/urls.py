from django.urls import path
from django.conf.urls import url

from . import views

app_name = "gematriacore"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    url(
        regex=r'^words/$',
        view=views.WordListView.as_view(),
        name='words'
    ),
    url(
        regex=r'^dictionary/(?P<pk>\d+)$',
        view=views.DictionaryDetailView.as_view(),
        name='dict_detail'
    ),
    url(
        regex=r'^dictionary(?P<pk>\d+)/results/$',
        view=views.DictionaryDetailView.as_view(),
        name='results'
    ),
    url(
        regex=r'^dictionary(?P<pk>\d+)/update/$',
        view=views.DictionaryDetailView.as_view(),
        name='update'
    )
]
