from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def programmes(request):
    context = {
        'courses': [
            {'name': 'software engineering', 'duration': 6, 'level': 'advanced'},
            {'name': 'data science', 'duration': 5, 'level': 'intermediate'},
            {'name': 'cyber security', 'duration': 4, 'level': 'beginner'},
        ],
        'school_name': 'Zindua School'
    }
    return render(request, 'programmes.html', context)