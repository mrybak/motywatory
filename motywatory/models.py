from django.db import models

from djangotoolbox.fields import EmbeddedModelField
from django.contrib.auth.models import User

from motywatory.gridfsuploads import gridfs_storage


class Motivator(models.Model):
    text = models.TextField()
    author = EmbeddedModelField(User)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(storage=gridfs_storage, upload_to='.', blank=True)
    # https://github.com/mdirolf/nginx-gridfs
