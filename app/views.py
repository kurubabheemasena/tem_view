from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class CBVcontext(TemplateView):
    template_name='context.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='bheema'
        context['age']=24
        context['address']='bennikal'
        return context
