
from django.urls import include, path

from . import views
from .views import StudentList ,StudentDetail, BlokList, BlokDetail, ToetsList, ToetsDetail ,CijferList, CijferDetail

urlpatterns = [

    path("student/", StudentList.as_view()),
    path("student/<pk>", StudentDetail.as_view()),

    path("blok/", BlokList.as_view()),
    path("blok/<pk>", BlokDetail.as_view()),

    path("toets/", ToetsList.as_view()),
    path("toets/<pk>", ToetsList.as_view()),

    path("cijfer/", CijferList.as_view()),
    path("cijfer/<pk>", CijferDetail.as_view()),
]