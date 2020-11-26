from django.db import models


class Blok(models.Model):
    blok = models.CharField(max_length=45, default='')
    jaar = models.IntegerField(default=1)

    def __str__(self):
        # zet de naam van de entry als blok
        return self.blok


class Toets(models.Model):
    toets_code = models.CharField(max_length=45, default='')
    toets_naam = models.CharField(max_length=45, default='')
    jaar = models.IntegerField(default=0)
    blok = models.ForeignKey(Blok, on_delete=models.CASCADE, default=0)
    volgorde = models.IntegerField(default=1)

    def __str__(self):
        # zet de naam van de entry als toets_code
        return self.toets_code


class Student(models.Model):
    voornaam = models.CharField(max_length=10, default='')
    achternaam = models.CharField(max_length=10, default='')
    student_nummer = models.IntegerField(default=0)

    def __str__(self):
        # zet de naam van de entry als voornaam
        return self.voornaam


class Cijfer(models.Model):
    voldoende = models.BooleanField(default=False)
    blok = models.ForeignKey(Blok, on_delete=models.CASCADE, default=0)
    toets_code = models.ForeignKey(Toets, on_delete=models.CASCADE, default=0, related_name='toetsCode')
    toets_naam = models.ForeignKey(Toets, on_delete=models.CASCADE, default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)
    datum_toets = models.CharField(max_length=10, default="00-00-2020")

    def __str__(self):
        # zet de naam van de entry als "blok - voldoende"
        return "%s" % self.blok + " - %s" % self.voldoende
