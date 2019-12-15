from django.urls import include, path
from django.conf.urls import url

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "gematriacore"


# router = routers.DefaultRouter()
# router.register(r'groups', views.GroupViewSet)
# router.register(r'wj', views.GroupViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
#     path('home', views.HomeView.as_view(), name="home"),
#     url(r'^api-auth/', include('rest_framework.urls')),
# ]

router = routers.DefaultRouter()
router.register(r'alphabets', views.AlphabetViewSet)
router.register(r'words', views.WordViewSet)
router.register(r'word-values', views.WordValueViewSet)
router.register(r'word-meanings', views.WordMeaningViewSet)
router.register(r'gematria-methods', views.GematriaMethodViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'languages', views.LanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('words/<int:pk>/num-value', views.WordNumericalValue.as_view(), name='word-value'),
    path('suggestions', views.SuggestionsView.as_view(), name='suggestions'),
]

urlpatterns += router.urls
