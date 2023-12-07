from django.db import models


class intents(models.Model):
    tag = models.CharField(max_length=255)
    value = models.CharField(max_length=1024)


class response(models.Model):
    tag = models.CharField(max_length=255)
    response = models.CharField(max_length=1024)


class config(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

class website(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=4096)
    note = models.IntegerField()
    url = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024)
    security = models.CharField(max_length=4096)
    voted = models.IntegerField(default = 0)



