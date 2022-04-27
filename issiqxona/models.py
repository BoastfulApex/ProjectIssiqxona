from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class Question(models.Model):
    question = models.TextField(max_length=500, null=True, blank=True)
    answer = models.TextField(max_length=500, null=True, blank=True)


class Stories(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
