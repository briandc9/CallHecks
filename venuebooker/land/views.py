from django.shortcuts import render
from django.http import HttpResponse

events = [
    {
        'name': 'Ye',
        'performance_date': 'November 4, 2018'
    }
]


def home(request):
    #return HttpResponse('<h1>Venue Booker Home</h1>')
    context = {
        'events': events
    }
    return render(request, 'land/home.html', context)

def about(request):
    return render(request, 'land/about.html')
# Create your views here.
