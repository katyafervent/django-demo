from django.shortcuts import render, get_object_or_404

from .models import Workshop


def index(request):
    workshops = Workshop.objects.all()
    return render(request, 'workshops/index.html', {
        'workshops': workshops
    })


def workshop_detail(request, workshop_slug):
    selected_workshop = get_object_or_404(Workshop, slug=workshop_slug)

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
