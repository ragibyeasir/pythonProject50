from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField(max_length=1000)
	category = models.CharField(max_length=200)





def __str__(self):
	return self.title
