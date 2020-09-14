from django.db import models

# Create your models here.


class Toets(models.Model):
    toets = models.CharField(max_length=45, default='')

    def __str__(self):
        return self.toets


class Blok(models.Model):
    blok = models.CharField(max_length=45, default='')
    toetsen = models.ManyToManyField(Toets)

    def __str__(self):
        return self.blok


class Cijfer(models.Model):
    cijfer = models.FloatField(default=0) # is double in sql + ERD
    blok = models.ForeignKey(Blok, on_delete=models.CASCADE)
    toets = models.ForeignKey(Toets, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.blok + " - %s" % self.toets


class Student (models.Model):
    voornaam = models.CharField(max_length=45, default='')
    achternaam = models.CharField(max_length=45, default='')
    cijfers = models.ManyToManyField(Cijfer)

    def __str__(self):
        return self.voornaam
