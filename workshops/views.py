from django.shortcuts import render

from .models import Workshop


def index(request):
    workshops = Workshop.objects.all()
    return render(request, 'meetups/index.html', {
        'workshops': workshops
    })


def workshop_details(request, workshop_slug):
    try:
        selected_workshop = Workshop.objects.get(slug=workshop_slug)
        context = {
            'workshop_found': True,
            'workshop_title': selected_workshop.title,
            'workshop_description': selected_workshop.description
        }
        return render(
            request,
            'workshops/workshop_details.html',
            context
        )
    except Exception:
        context = {'workshop_found': False}
        return render(
            request,
            'workshops/workshop_details.html',
            context
        )
