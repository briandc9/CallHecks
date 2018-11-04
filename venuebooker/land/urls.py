from django.urls import path
from . import views

urlpatterns = [
    #path('route', view.function, name='booker-something'),
    path('', views.home, name='booker-home'),
    path('about', views.about, name='booker-about'),

]
