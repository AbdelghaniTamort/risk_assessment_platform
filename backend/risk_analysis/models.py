from django.contrib.gis.db import models



class RiskZone(models.Model):
    name = models.CharField(max_length=100)
    risk_type = models.CharField(max_length=50)  # inondation, séisme...
    geometry = models.GeometryField(srid=4326)
    severity = models.FloatField()

class PropertyAssessment(models.Model):
    address = models.TextField()
    location = models.PointField(srid=4326)
    risk_score = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
