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
        context['subject'] = 'HKU ID: ' + uid
        context['date'] = date

        tmp = requests.get('https://intense-brushlands-34756.herokuapp.com/core/api/close-contacts/' + uid +'/' + date +'/')
        members = tmp.json()
        ret = set()
        for member in members:
            ret.add(member['hku_id'])

        context['contacts'] = sorted(ret)

        return context

class VenueView(TemplateView):
    template_name = "venues.html"

    def get_context_data(self, **kwargs):
        uid = self.kwargs['id']
        date = self.kwargs['date']
        context = super().get_context_data(**kwargs)
        context['subject'] = 'HKU ID: ' + uid
        context['date'] = date
        tmp = requests.get('https://intense-brushlands-34756.herokuapp.com/core/api/venues-visited-by/' + uid +'/' + date +'/')

        venues = tmp.json()
        ret = set()
        for venue in venues:
            code = venue['venue']
            venue_info_tmp = requests.get('https://intense-brushlands-34756.herokuapp.com/core/api/venues/' + code + '/')
            venue_info = venue_info_tmp.json()
            location = venue_info['location']
            ret.add(location)

        context['venues'] = sorted(ret)
        return context
