from django.urls import path, include
from . import views
import rest_api
from rest_framework import routers


router = routers.DefaultRouter()
router.register('TG_user', views.TG_userView)
router.register('Note', views.NoteView)

urlpatterns = [
    path('', include(router.urls))
]
