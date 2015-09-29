from django.db import models

# Create your models here.
class Reviews(models.Model):
	username = models.CharField(max_length=100)
	rating = models.CharField(max_length=10)
	note = models.TextField()
	companyid = models.CharField(max_length=200)
	sourceid = models.CharField(max_length=200)
	class Meta:
		db_table = "scrape_data"

class Urls(models.Model):
	url= models.URLField(max_length=200)
