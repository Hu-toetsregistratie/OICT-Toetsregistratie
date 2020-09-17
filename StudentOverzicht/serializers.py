from rest_framework import serializers
from .models import Student, Blok, Cijfer, Toets






class Blokserializer(serializers.ModelSerializer):
    class Meta:
        model = Blok
        fields = ('id', 'blok')


class Student_Naam(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('voornaam', 'achternaam')


class Cijferserializer(serializers.ModelSerializer):
    student = Student_Naam()
    toets = serializers.StringRelatedField()
    blok = serializers.StringRelatedField()

    class Meta:
        model = Cijfer
        fields = ('id', 'cijfer', 'toets', 'blok', 'student')


class Toetsserializer(serializers.ModelSerializer):
    class Meta:
        model = Toets
        fields = ('id', 'toets')


class Studentserializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'voornaam', 'achternaam')