from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import ClienteForm

# Create your views here.

@login_required
def clients(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'clientes/clientes.html', context)


@login_required
def client(request, id):
    person = Person.objects.get(pk=id)
    context = {
        'person': person
    }
    return render(request, 'clientes/detalhes.html', context)


@login_required
def new_client(request):
    form = ClienteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('clientes:clients')

    return render(request, 'clientes/novo.html', {'form': form})


@login_required
def update_client(request, id):
    client = get_object_or_404(Person, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('clientes:clients')
    
    return render(request, 'clientes/editar.html', {'form': form})


@login_required
def delete_client(request, id):
    client = get_object_or_404(Person, pk=id)
    if client:
        client.delete()
    return redirect('clientes:clients')