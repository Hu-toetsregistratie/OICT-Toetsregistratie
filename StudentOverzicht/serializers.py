from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

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

    def create(self, validated_data):
        return Cijfer(**validated_data)

    class Meta:
        model = Cijfer
        fields = ('id', 'cijfer', 'toets', 'blok', 'student')


class Cijfer_ID_serializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Cijfer.objects.all())
    toets = serializers.PrimaryKeyRelatedField(queryset=Cijfer.objects.all())
    blok = serializers.PrimaryKeyRelatedField(queryset=Cijfer.objects.all())


    class Meta:
        model = Cijfer
        fields = ('id', 'voldoende', 'toets', 'blok', 'student')


class Toetsserializer(serializers.ModelSerializer):
    class Meta:
        model = Toets
        fields = ('id', 'toets_code')


class Studentserializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'voornaam', 'achternaam')