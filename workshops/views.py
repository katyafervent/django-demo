from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    workshops = [
        { 
            'title': 'A First Workshop', 
            'location': 'New York', 
            'slug': 'a-first-workshop' 
        },
        { 
            'title': 'A Second Workshop', 
            'location': 'Paris', 
            'slug': 'a-second-workshop' 
        }
    ]

    return render(request, 
                  'workshops/index.html', 
                  {'workshops': workshops}
                  )

def workshop_detail(request, workshop_slug):
    print(workshop_slug)
    selected_workshop = {
        'title': 'A First Workshop', 
        'description': 'This is the first workshop!'
        }
    return render(request, 
                  'workshops/workshop_details.html',
                  {
                      'workshop_title': selected_workshop['title'],
                      'workshop_descrioption': selected_workshop['description']
                  }
            )