from django.db import models


# Create your models here.


class Test(models.Model):
    Student = models.TextField(default='')
    Jaar = models.TextField(default='')
    Toets = models.TextField(default='')
    Behaald = models.BooleanField(default=False)
