from django.db import models

# Create your models here.


class BasisStudent (models.Model):
    Student = models.TextField(max_length=30, default='')
    Jaar = models.IntegerField(default=0)
    Toets = models.IntegerField(default=0)
    Behaald = models.BooleanField(default=False)