from django.views.generic import ListView
from ..models import Menu
# from ..forms import *


class Index(ListView):
    '''
    Отображает главную страницу и отображает 1000 слов в виде зеленых точек,
    красные точки отображают выученные слова.
    '''
    model = Menu
    template_name = 'guitar_school/index.html'
    # context_object_name = 'words_counter_home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        # return dict(list(context.items()) + list(var.items()))

