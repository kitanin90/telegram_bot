from django.shortcuts import render
from rest_framework import viewsets
from .models import TG_user, Note
from .serializers import TG_userSerializer, NoteSerializer


class TG_userView(viewsets.ModelViewSet):
    queryset = TG_user.objects.all()
    serializer_class = TG_userSerializer


class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

