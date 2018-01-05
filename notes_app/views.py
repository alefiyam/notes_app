from django.shortcuts import redirect
from models import *
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def home(request):
    notes = Notes.objects.all()
    return render(request, 'home.html', {'notes': notes})

def add_notes(request):
    text = request.POST['text']
    if text != "":
        notes = Notes.objects.create(text = text)
        notes.save()
        notes = Notes.objects.all()
        text = ""
        return render(request, 'home.html', {'notes': notes})
    else:
        return home(request)

def show_notes(request): 
    notes_id = request.GET['id']
    notes_obj = Notes.objects.get(id = notes_id)
    import json
    return HttpResponse(json.dumps({"notes_obj":notes_obj.text}), content_type='application/json')
            