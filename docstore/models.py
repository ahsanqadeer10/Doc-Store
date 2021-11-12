from django.db import models

# Create your models here.

class Folder(models.Model):
      name = models.CharField(max_length=100, unique=True, null=False)
      topic = models.ManyToManyField("Topic", related_name="folders")

class Document(models.Model):
      name = models.CharField(max_length=100, unique=True, null=False)
      folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="documents")
      topic = models.ManyToManyField("Topic", related_name="documents")

class Topic(models.Model):
      name = models.CharField(max_length=100, unique=True, null=False)
