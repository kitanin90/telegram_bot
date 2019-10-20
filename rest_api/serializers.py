from rest_framework import serializers
from .models import TG_user, Note


class TG_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = TG_user
        fields = ('id', 'name', 'age', 'tg_chat_id')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('tg_user', 'text')
