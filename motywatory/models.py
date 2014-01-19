from django.db import models

from djangotoolbox.fields import EmbeddedModelField
from django.contrib.auth.models import User


class Motivator(models.Model):
    text = models.TextField()
    author = EmbeddedModelField(User)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
