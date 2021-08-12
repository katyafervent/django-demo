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
    show_workshops = True
    return render(request, 
                  'workshops/index.html', 
                  {'workshops': workshops,
                   'show_workshops': show_workshops}
                  )
