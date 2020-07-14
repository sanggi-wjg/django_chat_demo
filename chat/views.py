import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    return render(request, template_name = 'chat/index.html')


def room(request, room_name):
    return render(request, template_name = 'chat/room.html', context = {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
