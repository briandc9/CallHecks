from django.shortcuts import render
from django.http import HttpResponse
from .models import Event


events = [
    {
        'name': 'Ye',
        'concert': 'Final Countdown',
        'performance_date': 'November 4, 2018'
    }
]


def home(request):
    #return HttpResponse('<h1>Venue Booker Home</h1>')
    context = {
        'events': Event.objects.all().sort_by('performance_date')
    }
    return render(request, 'land/home.html', context)

def about(request):
    return render(request, 'land/about.html')
# Create your views here.
