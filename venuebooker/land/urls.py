from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='booker-home'),
    path('about', views.about, name='booker-about'),
]
