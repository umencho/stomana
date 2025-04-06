from django.db import models
from django.utils import timezone

class TypeIncident(models.Model):
    type_name = models.CharField(max_length=100, choices=[
        ('Incident', 'Incident'),
        ('Near miss', 'Near miss')
    ])
 
    def __str__(self):
        return self.type_name
    
class Area(models.Model):
    location = models.CharField(max_length=100, choices=[
        ('Scrap yard', 'Scrap yard'),
        ('Meltshop', 'Meltshop'),
        ('Rolling mill', 'Rolling mill'),
        ('Plate mill', 'Plate mill'),
        ('250', '250'),
        ('Prosal', 'Prosal'),
        ('TKC', 'TKC'),
        ('Other', 'Other'),
        ('Unknown', 'Unknown')
    ])
    area_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.location} - {self.area_name}"

class Incident(models.Model):
    LOCATION_CHOICES = [
        ('Scrap yard', 'Scrap yard'),
        ('Meltshop', 'Meltshop'),
        ('Rolling mill', 'Rolling mill'),
        ('Plate mill', 'Plate mill'),
        ('250', '250'),
        ('Prosal', 'Prosal'),
        ('TKC', 'TKC'),
        ('Other', 'Other'),
        ('Unknown', 'Unknown')
    ]

    title = models.CharField(max_length=100)
    incident_type = models.ForeignKey('TypeIncident', on_delete=models.CASCADE, related_name='incidents', default=1)
    date = models.DateTimeField(auto_now_add=True)
    date_incident = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='Unknown')
    area = models.CharField(max_length=100,default=1)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
    
    @property
    def since(self):
         return (timezone.now() - self.date).days
    