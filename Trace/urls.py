from django.template.defaulttags import url
from django.urls import path
from Trace import views

urlpatterns = [
    path('contacts', views.ContactView.as_view()),
    path('venues', views.VenueView.as_view()),
]