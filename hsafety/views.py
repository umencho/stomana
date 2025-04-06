#from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

def homepage(request):
    #return HttpResponse('Stomana Safety')
    return render(request, 'home.html')




