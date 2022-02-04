from django.contrib.auth import get_user_model
from django.db import models

from main.models import AutoPost

User = get_user_model()


class RentAuto(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rent')
    post = models.ForeignKey(AutoPost, on_delete=models.CASCADE, related_name='rent')
    info = models.TextField(default='Bishkek')

    def __str__(self):
        return self.post.title