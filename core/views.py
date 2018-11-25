from django.views.generic import TemplateView

from core.models import FirstPageProjects, Project


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['first_page_projects'] = FirstPageProjects.load().projects.all()
        return context


class ProjectView(TemplateView):
    template_name = 'ProjectItem.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(id=context.get('project_id'))
        return context


index_view = IndexView.as_view()
project_view = ProjectView.as_view()
