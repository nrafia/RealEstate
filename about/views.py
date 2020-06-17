from django.shortcuts import render
from .models import About, History


def about_us(requests):
    about_us = About.objects.all()
    history_all = History.objects.all()

    template = 'about/about.html'
    context = {
        'about_us': about_us,
        'history_all': history_all
    }

    return render(requests, template, context)
