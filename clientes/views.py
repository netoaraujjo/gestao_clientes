from django.shortcuts import render

from .models import Person

# Create your views here.

def clients(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'clientes/clientes.html', context)


def client(request, id):
    person = Person.objects.get(pk=id)
    context = {
        'person': person
    }
    return render(request, 'clientes/detalhes.html', context)