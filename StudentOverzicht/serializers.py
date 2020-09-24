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
    toets_code = serializers.StringRelatedField()
    blok = serializers.StringRelatedField()

    def create(self, validated_data):
        return Cijfer(**validated_data)

    class Meta:
        model = Cijfer
        fields = ('id', 'voldoende', 'toets_code', 'blok', 'student')


class Cijfer_ID_serializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    toets_code = serializers.PrimaryKeyRelatedField(queryset=Toets.objects.all())
    blok = serializers.PrimaryKeyRelatedField(queryset=Blok.objects.all())


    class Meta:
        model = Cijfer
        fields = ('id', 'toets_code', 'blok', 'student','voldoende')


class Toetsserializer(serializers.ModelSerializer):
    class Meta:
        model = Toets
        fields = ('id', 'toets_code', 'toets_naam', 'jaar', 'blok')


class Studentserializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'voornaam', 'achternaam')


class Toets_Full(serializers.ModelSerializer):

    class Meta:
        model = Toets
        fields = ('id', 'toets_code', 'toets_naam', 'jaar')