from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import Studentserializer, Blokserializer, Cijferserializer, Toetsserializer
from StudentOverzicht.models import Student, Blok, Cijfer, Toets

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer


class StudentDetail(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

##############################################

class BlokList(ListAPIView):
    queryset = Blok.objects.all()
    serializer_class = Blokserializer


class BlokDetail(RetrieveAPIView):
    queryset = Blok.objects.all()
    serializer_class = Blokserializer

##############################################
class CijferList(ListAPIView):
    queryset = Cijfer.objects.all()
    serializer_class = Cijferserializer


class CijferDetail(RetrieveAPIView):
    queryset = Cijfer.objects.all()
    serializer_class = Cijferserializer

##############################################

class ToetsList(ListAPIView):
    queryset = Toets.objects.all()
    serializer_class = Toetsserializer


class ToetsDetail(RetrieveAPIView):
    queryset = Toets.objects.all()
    serializer_class = Toetsserializer