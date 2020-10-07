from django.shortcuts import render
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import Studentserializer, Blokserializer, Cijferserializer, Toetsserializer, Cijfer_ID_serializer, Toets_Full
from Main.models import Student, Blok, Cijfer, Toets
from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.
class StudentList(viewsets.ModelViewSet):
    serializer_class = Studentserializer
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','voornaam', 'achternaam', 'student_nummer']




class StudentDetail(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','voornaam', 'achternaam', 'student_nummer']


##############################################

class BlokList(viewsets.ModelViewSet):
    queryset = Blok.objects.all()
    serializer_class = Blokserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','blok']

class BlokDetail(viewsets.ModelViewSet):
    queryset = Blok.objects.all()
    serializer_class = Blokserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','blok']

##############################################
class CijferList(viewsets.ModelViewSet):
    queryset = Cijfer.objects.all()
    serializer_class = Cijferserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'voldoende', 'toets_code', 'blok', 'student']


class CijferDetail(viewsets.ModelViewSet):
    queryset = Cijfer.objects.all()
    serializer_class = Cijferserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'voldoende', 'toets_code', 'blok', 'student']

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



class Toets_Full(viewsets.ModelViewSet):
    queryset = Toets.objects.all()
    serializer_class = Toets_Full
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'toets_code', 'toets_naam', 'jaar']