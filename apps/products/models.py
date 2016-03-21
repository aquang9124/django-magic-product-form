from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Manufacturer(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField()
	class Meta:
		db_table = 'manufacturers'

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	description = models.TextField()
	created_at = models.DateTimeField()
	manufacturer = models.ForeignKey(Manufacturer)
	class Meta:
		db_table = 'products'
