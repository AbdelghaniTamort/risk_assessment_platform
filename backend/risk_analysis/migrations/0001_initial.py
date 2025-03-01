# Generated by Django 5.1.6 on 2025-02-25 22:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('risk_score', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RiskZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('risk_type', models.CharField(max_length=50)),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('severity', models.FloatField()),
            ],
        ),
    ]
