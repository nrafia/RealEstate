from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count
from .models import Property, States
from .forms import ReserveForm


def property_list(request):

    property_list = Property.objects.all()
    state_list = States.objects.annotate(property_count=Count('property')).values('name', 'property_count', 'image',
                                                                                  'id')
    #state_list = States.objects.all()
    template = 'properties/list.html'

    address_query = request.POST.get('q')
    print(address_query)
    property_type = request.POST.getlist('property_type', None)
    print(property_type)
    if address_query and property_type:
        property_list = property_list.filter(
            Q(name__icontains=address_query) &
            Q(type__icontains=property_type[0])
        ).distinct()

    context = {
        'property_list': property_list,
        'state_list': state_list,
    }
    return render(request, template, context)


def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'properties/detail.html'

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            instance = reserve_form.save(commit=False)
            instance.ads_id = property_detail.ads_id
            print(instance.ads_id)
            instance.save()
    else:
        reserve_form = ReserveForm()

    context = {
        'property_detail': property_detail,
        'reserve_form': reserve_form
    }

    return render(request, template, context)


def property_neighbors(request, id):
    property_neighbors = Property.objects.all().filter(state=id)
    #state_list = States.objects.all()
    state_list = States.objects.annotate(property_count=Count('property')).values('name', 'property_count', 'image',
                                                                                  'id')
    template = 'properties/list_neighbors.html'
    context = {
        'property_neighbors': property_neighbors,
        'state_list': state_list
    }

    return render(request, template, context)
