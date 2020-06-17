from django.shortcuts import render, redirect
from .models import ContactDetails
from .forms import ContactForm
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse, HttpResponseRedirect

def contact_us(request):
    contact_us = ContactDetails.objects.all()
    template = 'contact/contact.html'

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            from_email = contact_form.cleaned_data['from_email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

        try:
            sm(subject, message, from_email=['test@gmail.com'],recipient_list=['admin@admin.com'])

        except BadHeaderError:
            return HttpResponse('invalid Header')

        return redirect('contact:success')

    else:
        contact_form = ContactForm()

    context = {
        'contact_us': contact_us,
        'contact_form': contact_form,
    }

    return render(request, template, context)


def success(request):
    return HttpResponse('Message Sent Successfully')
