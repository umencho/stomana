from django.contrib import admin
from django.urls import path, include
from . import views
from incident import views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('incident/', include('incident.urls')),
    path('favicon\.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('contact/', views.contact, name='contact'),
    path('latest_incident/', views.latest_incident, name='last'),
    ]
