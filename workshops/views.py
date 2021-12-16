from django.shortcuts import get_object_or_404, render

from .models import Workshop


def index(request):
    workshops = Workshop.objects.all()
    return render(request, 'workshops/index.html', {'workshops': workshops})


def workshop_detail(request, workshop_slug):
    selected_workshop = get_object_or_404(Workshop, slug=workshop_slug)

    context = {'workshop': selected_workshop}
    return render(request, 'workshops/workshop_details.html', context)
