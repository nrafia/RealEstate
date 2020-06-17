from django.shortcuts import render
from django.db.models import Count
from properties.models import Property, States
from agents.models import Agents
from about.models import History
from .models import Highlights, Services
from about.models import History, About


def home(request):
    state_list = States.objects.annotate(property_count=Count('property')).values('name', 'property_count', 'image', 'id')
    highlights = Highlights.objects.all()
    agents = Agents.objects.all()
    property_list = Property.objects.all()
    history_all = History.objects.all()
    services_list = Services.objects.all()

    template = 'home/home.html'
    context = {
        'state_list': state_list,
        'highlights': highlights,
        'agents': agents,
        'property_list': property_list,
        'history_all': history_all,
        'services_list': services_list,
    }

    return render(request, template, context)