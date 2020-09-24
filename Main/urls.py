
from django.urls import include, path

from . import views
from .views import StudentList ,StudentDetail, BlokList, BlokDetail, ToetsList, ToetsDetail ,CijferList, CijferDetail
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'student', views.StudentList)
router.register(r'toets', views.ToetsList)
router.register(r'blok', views.BlokList)
router.register(r'cijfer', views.CijferList)
router.register(r'cijferid', views.Cijfer_ID)
router.register(r'toets_full', views.Toets_Full)


urlpatterns = [

    path('', include(router.urls)),

    #path("student/", views.StudentList()),
    #path("student/<pk>", views.StudentDetail),

    #path("blok/", BlokList.as_view()),
    #path("blok/<pk>", BlokDetail.as_view()),

    #path("toets/", ToetsList.as_view()),
    #path("toets/<pk>", ToetsList.as_view()),

    #path("cijfer/", CijferList.as_view()),
    #path("cijfer/<pk>", CijferDetail.as_view()),
]