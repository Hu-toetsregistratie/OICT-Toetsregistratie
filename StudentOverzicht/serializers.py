from rest_framework import serializers
from .models import Student, Blok, Cijfer, Toets



class Studentserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'voornaam', 'achternaam')



class Blokserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blok
        fields = ('id', 'blok')





class Cijferserializer(serializers.HyperlinkedModelSerializer):
    student = serializers.StringRelatedField()
    toets = serializers.StringRelatedField()
    blok = serializers.StringRelatedField()

    class Meta:
        model = Cijfer
        fields = ('id', 'cijfer', 'toets', 'blok', 'student')





class Toetsserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Toets
        fields = ('id', 'toets')
