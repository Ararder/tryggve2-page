from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  render
from datetime import datetime
from django.views.generic import TemplateView

from tryggve.models import Person, Country

# Create your views here.
# def home(request):
#     return HttpResponse("Hello, Tryggve")

class TestView(TemplateView):
    template_name = 'tryggve/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tp'] = Person.objects.all()
        return context



class CountryView(TemplateView):
    template_name = "tryggve/country_view.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country =  Country.objects.get(id=self.kwargs['pk'])
        # find the teamlead in the country
        try:
            context['teamlead'] = Person.objects.get(in_country=country, team_lead=True)
        except:
            context['teamlead'] = ''
        context['country_name'] = country.name
        context['tp'] = Person.objects.filter(in_country=country, team_lead=False)
        return context


