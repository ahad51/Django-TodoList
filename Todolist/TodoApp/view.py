from django.shortcuts import render,redirect
from .models import Mytodo
from .forms import TodoForm

def alltodos(request):
    tasks = Mytodo.objects.all()
    form=TodoForm
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'alltodo.html', {'tasks': tasks , 'form':form})

def deleteItem(request,pk):
    task=Mytodo.objects.get(id=pk)
    task.delete()
    return redirect('alltodos')
