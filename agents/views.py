from django.shortcuts import render

from .models import Agents


def agents(request):
    agents = Agents.objects.all()
    template = 'agents/agents.html'
    context = {
        'agents': agents
    }
    return render(request, template, context)
