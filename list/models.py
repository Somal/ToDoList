from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
	user = models.ForeignKey(User)
	task = models.CharField(max_length=500)
	condition = models.CharField(max_length=100, choices=('active', 'done'), default='active')
