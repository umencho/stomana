# Generated by Django 4.2.20 on 2025-04-05 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0003_typeincident'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='incident_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='incidents', to='incident.typeincident'),
        ),
        migrations.AlterField(
            model_name='typeincident',
            name='type_name',
            field=models.CharField(choices=[('Incident', 'Incident'), ('Near miss', 'Near miss')], max_length=100),
        ),
    ]
