from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    template = loader.get_template('chatapp/index.html')
    return HttpResponse(template.render({}, request))


def room(request, room_name):
    return render(request, 'chatapp/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })