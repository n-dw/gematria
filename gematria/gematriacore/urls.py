from django.urls import include, path
from django.conf.urls import url

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "gematriacore"


router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'wj', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('home', views.HomeView.as_view(), name="home"),
    url(r'^api-auth/', include('rest_framework.urls')),
]

format_patterns = [
    path('words/', views.WordList.as_view()),
    path('words/<int:pk>/', views.WordDetail.as_view()),
]
urlpatterns = urlpatterns + format_suffix_patterns(format_patterns)
