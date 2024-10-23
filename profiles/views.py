from django.views.generic import DetailView

from my_music_app_exam_prep.utils import get_user_obj


class ProfileDetailView(DetailView):

    template_name = 'profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()