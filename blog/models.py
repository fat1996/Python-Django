# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Posts(models.Model):
	author = models.CharField(max_length = 30)
	title = models.CharField(max_length = 100)
	bodytext = models.TextField()
	#timestamp = models.DateTimeField()

	def __str__(self):  #this is a built-in method that returns the 
	#string representation of the object.
		return "Author: " + self.author + ", title: " + self.title + \
		", text: " + self.bodytext + "\n"

class Comments(models.Model):
	comment = models.TextField()
	#timestamp = models.DateTimeField()

	def __str__(self):  #this is a built-in method that returns the 
	#string representation of the object.
		return "Comment: " + self.comment + "\n"

class Subscribers(models.Model):
	subcriber_name = models.CharField(max_length = 100)
	subcriber_email = models.CharField(max_length = 200)

	def __str__(self):  #this is a built-in method that returns the 
	#string representation of the object.
		return "Subscriber name: " + self.subcriber_name + \
		", Subscriber email: " + self.subcriber_email + "\n"

