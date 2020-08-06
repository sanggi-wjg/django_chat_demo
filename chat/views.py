import json

from django.shortcuts import render
from django.utils.safestring import mark_safe

from chat.util import create_rand_string, print_green, print_yellow


def index(request):
    return render(request, template_name = 'chat/index.html')


def room(request, room_name):
    print(request.session.__dir__())

    if 'USER_UQ_ID' not in request.session.keys():
        uq_id = create_rand_string()
        request.session.setdefault('USER_UQ_ID', uq_id)

    else:
        uq_id = request.session.get('USER_UQ_ID')

    print_green(request.session.items())
    print_yellow(uq_id)

    return render(request, template_name = 'chat/room.html', context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'uq_id_json'    : mark_safe(json.dumps(uq_id))
    })
