from django.db import models

# Create your models here.
#  db name=crud001, superuser iha,123
class User(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    pwd=models.CharField(max_length=50)

