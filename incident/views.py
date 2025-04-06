from django.shortcuts import render, redirect
from .models import Incident
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
import json 
from .forms import IncidentForm, TypeIncidentForm

def posts_list(request):
    incidents_list = Incident.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'incident': incidents_list})

def contact(request):
    return render(request, 'about.html')

def latest_incident(request):
    last_incident = Incident.objects.latest('date')
    return render(request, 'latest_incident.html', {'incident': last_incident})
print(latest_incident)

def homepage(request):
    inc2025 = Incident.objects.filter(date__year=2025).count()

    try:
        last_incident = Incident.objects.latest('date')
        nr_days = (timezone.now() - last_incident.date).days
    except ObjectDoesNotExist:
        nr_days = 0

    incidents = Incident.objects.order_by('date')
    max_days = 0
    if incidents.count() > 1:
        for i in range(1, incidents.count()):
            days_diff = (incidents[i].date - incidents[i-1].date).days
            if days_diff > max_days:
                max_days = days_diff

    # Get location data
    location_data = list(Incident.objects.values('location').annotate(count=Count('location')).order_by('-count'))

    context = {
        'inc2025': inc2025 if inc2025 != 0 else 'No incidents in 2025',
        'nr_days': nr_days,
        'max_days': max_days,
        'last_incident': last_incident,
        'location_data': json.dumps(location_data)  # Convert to JSON string
    }
    return render(request, 'home.html', context)

def create_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'posts/incident_form.html', {'form': form})

def create_type_incident(request):
    if request.method == 'POST':
        form = TypeIncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('type_incident_list')
    else:
        form = TypeIncidentForm()
    return render(request, 'posts/type_incident_form.html', {'form': form})