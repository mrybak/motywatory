from django.db import models

from djangotoolbox.fields import EmbeddedModelField


class Motivator(models.Model):
    text = models.TextField()
    author = EmbeddedModelField('User')

class User(models.Model):
    name = models.CharField(max_length=50)
