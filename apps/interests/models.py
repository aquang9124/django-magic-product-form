from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Interest(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField()
	class Meta:
		db_table = 'interests'

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	age = models.IntegerField()
	occupation = models.CharField(max_length=255)
	created_at = models.DateTimeField()
	interest = models.ForeignKey(Interest)
	class Meta:
		db_table = 'users'
