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
router.register(r'words', views.WordViewSet)
router.register(r'word-values', views.WordValueViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'languages', views.LanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home', views.HomeView.as_view(), name="home"),
    path('words/<int:pk>/num-value', views.WordNumericalValue.as_view(), name='word-value'),
    path('suggestions', views.SuggestionsView.as_view(), name='suggestions'),
]

urlpatterns += router.urls

# format_patterns = [
#     path('words/', views.WordList.as_view()),
#     path('words/<int:pk>/', views.WordDetail.as_view()),
#     path('words/<int:pk>/num-value', views.WordNumericalValue.as_view(), name='word-value'),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]


#urlpatterns = urlpatterns + format_suffix_patterns(format_patterns)
