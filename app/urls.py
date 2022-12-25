from django.urls import path

from .views import index, IndexView, IndexListView


urlpatterns = [
    path('', index, name='index'),
    path('main', IndexView.as_view(), name='main'),
    path('list', IndexListView.as_view(), name='list'),
]
