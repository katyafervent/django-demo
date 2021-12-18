from django.shortcuts import get_object_or_404, render

from .forms import RegistrationForm
from .models import Workshop


def index(request):
    workshops = Workshop.objects.all()
    return render(request, 'workshops/index.html', {'workshops': workshops})


def workshop_detail(request, workshop_slug):
    selected_workshop = get_object_or_404(Workshop, slug=workshop_slug)
    if request.method == 'GET':
        registration_form = RegistrationForm()
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            participant = registration_form.save()
            selected_workshop.participants.add(participant)

    context = {'workshop': selected_workshop, 'form': registration_form}
    return render(request, 'workshops/workshop_details.html', context)
