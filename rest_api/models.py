from django.db import models


class TG_user(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    tg_chat_id = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)


class Note(models.Model):
    tg_user = models.ForeignKey(TG_user, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.tg_user)