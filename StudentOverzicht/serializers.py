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
    class Meta:
        model = Cijfer
        fields = ('id', 'cijfer', 'toets_id', 'blok_id', 'student_id')





class Toetsserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Toets
        fields = ('id', 'toets')
