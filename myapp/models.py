from distutils.command.upload import upload
from typing_extensions import Required
from django.db import models

# Create your models here.
class myModel(models.Model):
    image = models.ImageField(upload_to='images/')