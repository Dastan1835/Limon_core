from django.views.generic import TemplateView
from journal.models import Publication, AboutMe


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.filter(is_active=True),
            'hashtags_list': Publication.objects.all()
        }
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):

        context = {
            "about_Me": AboutMe.objects.first()
        }
        return context


class PublicationDetailView(TemplateView):
    template_name = 'publication_detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            "publication": Publication.objects.get(id=publication_pk)
        }
        return context
