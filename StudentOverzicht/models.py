from django.db import models

# Create your models here.

class Blok(models.Model):
    blok = models.CharField(max_length=45, default='')

    def __str__(self):
        return self.blok

class Toets(models.Model):
    toets = models.CharField(max_length=45, default='')

    def __str__(self):
        return self.toets


class Cijfer(models.Model):
    cijfer = models.IntegerField(default=0)
    blok = models.OneToOneField(Blok, on_delete=models.CASCADE, default=0)
    toets = models.OneToOneField(Toets, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "%s" % self.blok + " - %s" %self.toets


class Student (models.Model):
    voornaam = models.CharField(max_length=10, default='')
    achternaam = models.CharField(max_length=10, default='')
    cijfers = models.ManyToManyField(Cijfer)

    def __str__(self):
        return self.voornaam


