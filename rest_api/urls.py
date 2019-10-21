from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('TG_user', views.TG_userView)
router.register('Note', views.NoteView)
router.register('Reg_user', views.Reg_userView)

urlpatterns = [
    path('', include(router.urls))
]
