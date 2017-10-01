from django.db import models
from django.utils import timezone

# Create your models here.

class Feed(models.Model):
	title = models.CharField(max_length = 200)
	url = models.URLField()
	is_active = models.BooleanField(default = False)

class Article(models.Model):
	feed = models.ForeignKey(Feed)
	title = models.CharField(max_length = 200)
	url = models.URLField()
	description = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	publication_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.publication_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
