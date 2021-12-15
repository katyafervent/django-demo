from django.shortcuts import render

from .models import Workshop


def index(request):
    workshops = Workshop.objects.all()
<<<<<<< HEAD
    return render(request, 'workshops/index.html', {
=======
    return render(request, 'meetups/index.html', {
>>>>>>> b9e3d93b6dfc3bdeba0a177a30fce50e09b1c18e
        'workshops': workshops
    })


<<<<<<< HEAD
def workshop_detail(request, workshop_slug):
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
=======
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
>>>>>>> b9e3d93b6dfc3bdeba0a177a30fce50e09b1c18e
