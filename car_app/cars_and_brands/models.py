from django.db import models

class Brand(models.Model):
    make = models.CharField(max_length=255, unique=True)

    

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=255)
    year = models.CharField(max_length=4)

# To make fixtures, create a folder in the app's folder named "fixtures" and 
# a JSON file within the fixtures folder with the following format:
# NOTE: (keys and values must be double-quoted)
# List of dictionaries with keys of "model", "pk", and "fields"
# "model": "<app name>.<model(can be lowercase)>"
# "pk": <primary key number>,
# "fields": dictionary w/ keys of model attributes; values are the dummy data
# E.g.:
# [
#     {"model': 'cars_and_brands.brand',
#     "pk": 1,
#     "fields": {
#         "name": 'Toyota',
#         ""
#         }
#     }
# ]
# After fixture is created, in terminal run:
# python manage.py loaddata <filename witho out extension>
