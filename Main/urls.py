from django.conf.urls import url
from django.urls import include, path

from . import views
from rest_framework import routers
from rest_framework.authtoken import views as apiViews

router = routers.DefaultRouter()
router.register(r'student', views.StudentList)
router.register(r'toets', views.ToetsList)
router.register(r'blok', views.BlokList)
router.register(r'cijfer', views.CijferList)
router.register(r'cijferid', views.Cijfer_ID)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', apiViews.obtain_auth_token)
]
