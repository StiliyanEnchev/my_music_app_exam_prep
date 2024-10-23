from django import views
from django.urls import path, include

from albums.views import AlbumCreateView, AlbumEditView, AlbumDetailsView, AlbumDeleteView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('edit/', AlbumEditView.as_view(), name='edit-album'),
        path('details/', AlbumDetailsView.as_view(), name='album-details'),
        path('delete/', AlbumDeleteView.as_view(), name='delete-album')
    ]))
]