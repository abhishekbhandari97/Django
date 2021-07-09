from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("info", views.info, name='info'),
    path("contact", views.contact, name='contact'),
    path("team", views.team, name='team'),
    path("coaching", views.coaching, name='coaching'),
    path("location", views.location, name='location')
]
