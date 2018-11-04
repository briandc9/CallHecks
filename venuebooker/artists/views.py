from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist
#from project import scheduling as s

artists = [
    {
        'name': 'Ye',
        'concert': 'Final Countdown',
        'performance_date': 'November 4, 2018'
    }
]



# Create your views here.

def artist_view(request):
    return render(request, 'users/artists.html')