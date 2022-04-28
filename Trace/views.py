from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponse, HttpRequest
import requests

class ContactView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        uid = self.kwargs['id']
        date = self.kwargs['date']
        context = super().get_context_data(**kwargs)
        context['subject'] = 'Student UID: ' + uid
        context['date'] = date
        context['contacts'] = requests.get('https://intense-brushlands-34756.herokuapp.com/core/api/close-contacts/' + uid +'/' + date +'/')

        return context

class VenueView(TemplateView):
    template_name = "venues.html"

    def get_context_data(self, **kwargs):
        uid = self.kwargs['id']
        date = self.kwargs['date']
        context = super().get_context_data(**kwargs)
        context['subject'] = 'Student UID: ' + uid
        context['date'] = date
        context['venues'] = requests.get('https://intense-brushlands-34756.herokuapp.com/core/api/venues-visited-by/' + uid +'/' + date +'/')
        return context