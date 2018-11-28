from django.views.generic import TemplateView

from core.models import FirstPageProjects, Project, ContactUs, AboutUs


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


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


class ContactUsView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        context['contact'] = ContactUs.load()
        return context


class AboutUsView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        about_us = AboutUs.load()
        context['about'] = about_us
        context['slide_show_pictures'] = about_us.slide_show_pictures.all()
        context['awards'] = about_us.awards.all()
        context['founders'] = about_us.founders.all()
        context['artists'] = about_us.artists.all()
        context['clients'] = about_us.clients.all()
        context['services'] = about_us.services.all()
        return context


index_view = IndexView.as_view()
project_view = ProjectView.as_view()
portfolio_view = PortfolioView.as_view()
contact_view = ContactUsView.as_view()
about_view = AboutUsView.as_view()
