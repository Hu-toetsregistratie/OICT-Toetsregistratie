from django.db import models

# Create your models here.


class Toets(models.Model):
    toets_code = models.CharField(max_length=45, default='')
    toets_naam = models.CharField(max_length=45, default='')

    def __str__(self):
        return self.toets_code


class Blok(models.Model):
    blok = models.CharField(max_length=45, default='')
    toetsen = models.ManyToManyField(Toets)

    def __str__(self):
        return self.blok


class Student(models.Model):
    voornaam = models.CharField(max_length=10, default='')
    achternaam = models.CharField(max_length=10, default='')


    def __str__(self):
        return self.voornaam

class Cijfer(models.Model):
    voldoende = models.BooleanField(default=False)
    blok = models.ForeignKey(Blok, on_delete=models.CASCADE, default=0)
    toets_code = models.ForeignKey(Toets, on_delete=models.CASCADE, default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "%s" % self.blok + " - %s" % self.voldoende

