from django.urls import path

from . import views

urlpatterns = [
    path('workshops', views.index,  name='all-workshops'),
    path('workshops/<slug:workshop_slug>',
         views.workshop_detail,
         name='workshop-detail'),
]
