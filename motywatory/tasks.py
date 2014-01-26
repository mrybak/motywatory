from __future__ import absolute_import

from celery import shared_task
from jnp3.serializers import MotivatorSerializer
from motywatory.models import Motivator
from requests import Response
from rest_framework import status


@shared_task
def upload_motivator(text, img, author):
    print img.name
    motywator = Motivator.objects.create(text=text, img=img, author=author)
    # motywator.img.name = motywator.img.name.split('/')[1]
    # print motywator.img
    # print motywator.img.name.split('/')[1]
    # motywator.save()

