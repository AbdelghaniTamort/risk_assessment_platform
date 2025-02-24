from django.contrib.gis.db import models



class RiskZone(models.Model):
    RISK_TYPES = [
        ('flood', 'Inondation'),
        ('fire', 'Incendie'),
        ('earthquake', 'Séisme'),
    ]

    name = models.CharField(max_length=100)
    risk_type = models.CharField(max_length=20, choices=RISK_TYPES)
    risk_level = models.IntegerField()
    occurrence_probability = models.FloatField(help_text="Probabilité entre 0 et 1")
    geom = models.PolygonField()

    def __str__(self):
        return f"{self.name} ({self.get_risk_type_display()})"
