from django.contrib.auth import get_user_model
from django.db import models

from main.models import AutoPost

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    post = models.ForeignKey(AutoPost, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()

    def __str__(self):
        return self.post.title