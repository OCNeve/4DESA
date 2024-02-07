from datetime import datetime
from django.db import models
from django.db.models import CharField, DateTimeField, ForeignKey, CASCADE, BooleanField, TextField
from django.contrib.auth.models import User


class Profile(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    is_public = BooleanField(default=False)


class Posts(models.Model):
    creator = ForeignKey(User, on_delete=CASCADE)
    date = DateTimeField(null=False, default=datetime.now)
    text = TextField()


class Comments(models.Model):
    post = ForeignKey(Posts, on_delete=CASCADE)
    value = CharField(max_length=255, null=False)
    date = DateTimeField(unique=True, null=False, default=datetime.now)


class Images(models.Model):
    post = ForeignKey(Posts, on_delete=CASCADE)
    path = CharField(max_length=255, unique=True, null=False)


class Videos(models.Model):
    post = ForeignKey(Posts, on_delete=CASCADE)
    path = CharField(max_length=255, unique=True, null=False)


