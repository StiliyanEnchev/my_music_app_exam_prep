from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from albums.models import Album
from my_music_app_exam_prep.utils import get_user_obj
from profiles.forms import ProfileCreateForm


# Create your views here.

class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_user_obj()

        if profile:
            return ['home-with-profile.html']

        return ['home-no-profile.html']