from django.shortcuts import render
from .models import Mytodo

def alltodos(request):
    todos = Mytodo.objects.all()
    return render(request, 'alltodo.html', {'todos': todos})