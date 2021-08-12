from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('workshops', views.index),
    path('workshops/<slug:workshop_slug>', views.workshop_detail, name='workshop-detail'),
]
