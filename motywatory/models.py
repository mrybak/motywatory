from django.db import models

from djangotoolbox.fields import EmbeddedModelField


class Motivator(models.Model):
    text = models.CharField()
    author = EmbeddedModelField('User')

class User(models.Model):
    name = models.CharField()
