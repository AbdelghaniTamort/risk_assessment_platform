
from django.contrib.gis import admin  # Modification ici
from .models import RiskZone, PropertyAssessment

@admin.register(RiskZone)
class RiskZoneAdmin(admin.GISModelAdmin):  # Utilisez GISModelAdmin au lieu de OSMGeoAdmin
    list_display = ('name', 'risk_type', 'severity')

@admin.register(PropertyAssessment)
class PropertyAssessmentAdmin(admin.GISModelAdmin):
    list_display = ('address', 'risk_score', 'date_created')