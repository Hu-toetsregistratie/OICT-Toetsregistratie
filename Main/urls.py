from django.conf.urls import url
from django.urls import include, path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'student', views.StudentList)
router.register(r'toets', views.ToetsList)
router.register(r'blok', views.BlokList)
router.register(r'cijfer', views.CijferList)
router.register(r'cijferid', views.Cijfer_ID)
router.register(r'testtoets', views.Toets2)


urlpatterns = [
    path('', include(router.urls)),
]