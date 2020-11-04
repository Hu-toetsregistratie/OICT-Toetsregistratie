from django_filters.rest_framework import DjangoFilterBackend
from .serializers import Studentserializer, Blokserializer, Cijferserializer, Toetsserializer, Cijfer_ID_serializer
from Main.models import Student, Blok, Cijfer, Toets
from rest_framework import viewsets


class StudentList(viewsets.ModelViewSet):
    serializer_class = Studentserializer
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','voornaam', 'achternaam', 'student_nummer']

##############################################

class BlokList(viewsets.ModelViewSet):
    queryset = Blok.objects.all()
    serializer_class = Blokserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','blok']

##############################################
class CijferList(viewsets.ModelViewSet):
    queryset = Cijfer.objects.all()
    serializer_class = Cijferserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'voldoende', 'toets_code', 'blok', 'student', 'student__voornaam','student__student_nummer']

##############################################

class ToetsList(viewsets.ModelViewSet):
    queryset = Toets.objects.all()
    serializer_class = Toetsserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'toets_code', 'toets_naam', 'jaar', 'blok']


class ToetsDetail(viewsets.ModelViewSet):
    queryset = Toets.objects.all()
    serializer_class = Toetsserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'toets_code', 'toets_naam', 'jaar', 'blok']

###############################################
class Cijfer_ID(viewsets.ModelViewSet):
    queryset = Cijfer.objects.all()
    serializer_class = Cijfer_ID_serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'toets_code', 'blok', 'student','voldoende']
