from django import views
from django.urls import path

from albums.views import AlbumCreateView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='add-album')
]