from rest_framework import serializers

from .models import Student, Blok, Cijfer, Toets


class Blokserializer(serializers.ModelSerializer):#serializer voor de blok api
    class Meta:
        model = Blok
        fields = ('id', 'blok', 'jaar')


class Student_Naam(serializers.ModelSerializer):#serializer voor student in Cijfereserializer

    class Meta:
        model = Student
        fields = ('voornaam', 'achternaam', 'student_nummer')


class Cijferserializer(serializers.ModelSerializer):#serializer voor de Cijfer api
    student = Student_Naam()
    toets_code = serializers.StringRelatedField()
    blok = serializers.StringRelatedField()

    def create(self, validated_data):
        #functie om de data vanuit de serializers te valideren
        return Cijfer(**validated_data)

    class Meta:
        model = Cijfer
        fields = ('id', 'voldoende', 'toets_code', 'blok', 'student', 'datum_toets', "toets_naam")


class Cijfer_ID_serializer(serializers.ModelSerializer):#serializer voor de Cijfer ID's
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    toets_code = serializers.PrimaryKeyRelatedField(queryset=Toets.objects.all())
    blok = serializers.PrimaryKeyRelatedField(queryset=Blok.objects.all())
    toets_naam = serializers.PrimaryKeyRelatedField(queryset=Toets.objects.all())



    class Meta:
        model = Cijfer
        fields = ('id', 'voldoende', 'toets_code', 'blok', 'student', 'datum_toets',"toets_naam")


class Toetsserializer(serializers.ModelSerializer):#serializer voor de Toetsen

    blok = serializers.PrimaryKeyRelatedField(queryset=Blok.objects.all())

    class Meta:
        model = Toets
        fields = ('id', 'toets_code', 'toets_naam', 'jaar', 'blok')


class Studentserializer(serializers.ModelSerializer):#serializer voor Studenten

    class Meta:
        model = Student
        fields = ['id', 'voornaam', 'achternaam', 'student_nummer']
