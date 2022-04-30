from dataclasses import fields
from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=140)
    massage = models.CharField(max_length=25000)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['id']