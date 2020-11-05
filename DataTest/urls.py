"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views



import Main




urlpatterns = [
    path("", views.DataTest_Main),
    path("1", views.DataTest_Jaar_Toets_Resultaat_Pogingen),
    path("2", views.DataTest_blok),
    path("3", views.DataTest_student),
    path("4", views.DataTest_cijfer),
    path("G1", views.blok_gen),
    path("G2", views.run_toets_gen),
    path("G3", views.run_student_gen),
    path("G4", views.run_cijfer_gen),
    path("G5", views.graph_gen),
    path("G6", views.Run_all_gen_test),
    path("G7", views.stat_gen),



]


