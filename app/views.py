from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class GeneratorView(TemplateView):
    template_name = 'index.html'