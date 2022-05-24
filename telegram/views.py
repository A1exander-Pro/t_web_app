from django.views.generic import TemplateView


class WebAppView(TemplateView):
    template_name = 'webpage.html'

