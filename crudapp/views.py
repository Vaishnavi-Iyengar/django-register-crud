from django.shortcuts import render, redirect
from .models import Register
from .forms import RegisterForm

def index(request):
    form = RegisterForm()
    registers = Register.objects.all()  # <-- This must be here

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # <-- Redirect to show updated list

    return render(request, 'index.html', {'form': form, 'registers': registers})


def update(request, pk):
    record = Register.objects.get(id=pk)
    form = RegisterForm(instance=record)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form})

def delete(request, pk):
    record = Register.objects.get(id=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('index')
    return render(request, 'del.html', {'record': record})
