from django.urls import path

from profiles.views import ProfileDetailView

urlpatterns = [
    path('details/', ProfileDetailView.as_view(), name='profile-details'),
]