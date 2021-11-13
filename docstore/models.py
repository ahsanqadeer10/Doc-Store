from django.db import models

# Create your models here.

class Folder(models.Model):
      name = models.CharField(max_length=100, unique=True, blank=False)
      topic = models.ManyToManyField("Topic", related_name="folders", blank=True)

      def __str__(self):
            return self.name


class Document(models.Model):
      name = models.CharField(max_length=100, unique=True, blank=False)
      folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="documents")
      topic = models.ManyToManyField("Topic", related_name="documents", blank=True)

      def __str__(self):
            return self.name


class Topic(models.Model):
      name = models.CharField(max_length=100, unique=True, null=False)
      
      def __str__(self):
            return self.name
