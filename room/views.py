from django.shortcuts import render

from .models import Room

def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'rooms.html', {'rooms': rooms})
