from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
	newsid = models.CharField(max_length=20,blank=False)
	title = models.CharField(max_length=300)
	author = models.CharField(max_length=30, default="Anonymous", blank=False)
	
	text = models.CharField(max_length=5000, default="")
	
	label = models.IntegerField(default="0")
	def __str__(self):
		return self.author + ', ' + self.title

		#News 1  D1 T1
		#News 2  D1 T1