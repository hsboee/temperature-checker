from django.db import models
from datetime import datetime

# Create your models here.

class Date(models.Model):
	rec_date=models.DateField(blank=False, default=datetime.now().strftime("%Y-%m-%d"),primary_key=True)
	
	def __str__(self):
		return str(self.rec_date)


class Theom(models.Model):
	degree=models.FloatField()
	time  =models.TimeField(blank=False, primary_key=True)
	rec_date_index = models.ForeignKey(Date)


	def __str__(self):
		return "%s %s" % (self.time, self.degree)


