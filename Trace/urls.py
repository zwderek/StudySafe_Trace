from django.template.defaulttags import url
from django.urls import path
from Trace import views

urlpatterns = [
    path('contacts/<str:id>/<str:date>', views.ContactView.as_view()),
    path('venues/<str:id>/<str:date>', views.VenueView.as_view()),
]