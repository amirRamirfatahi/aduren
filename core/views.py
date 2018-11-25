from django.views.generic import TemplateView

from core.models import FirstPageProjects


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['first_page_projects'] = FirstPageProjects.load().projects.all()
        return context


index_view = IndexView.as_view()
