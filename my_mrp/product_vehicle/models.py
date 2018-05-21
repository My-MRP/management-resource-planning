from django.db import models


# Create your models here.
class Vehicle(models.Model):
    engines = (
        ('v6', '3.0-liter TFSI® turbocharged DOHC V6'),
        ('v8', '3.4 Prestige 3.0 TFSI® supercharged v8'),
        ('v10', '5.2-liter FSI® dual-injection V10'))

    colors = (
        ('white', 'Ibis White'),
        ('black', 'Mythos Black metallic'),
        ('blue', 'Ara Blue crystal'))

    packages = (
        ('default', 'Default'),
        ('confort', 'Confortable cushioned seats.'),
        ('premium', 'Premium Cocaine White Leather Seats'))

    systems = (
        ('sony', 'SONY Ultra Clear Sound System'),
        ('bose', 'BOSE Ultra Premium Sound System'),
        ('hk', 'Harmen Kardon Infinite Sound System'))

    model_name =        models.CharField(max_length=100, null=False)
    trim_engine =       models.CharField(max_length=2, choices=engines)
    exterior_color =    models.CharField(max_length=5, choices=colors)
    wheels =            models.CharField(max_length=10, choices=colors)
    interior_package =  models.CharField(max_length=10, choices=packages)
    audio_system =      models.CharField(max_length=15, choices=systems)
    bike_rack =         models.BooleanField(default=False)


class Engine(models.Model):
    engine_name =
    engine_description =  '3.4 Prestige 3.0 TFSI® supercharged v8'
    engine_cost =
