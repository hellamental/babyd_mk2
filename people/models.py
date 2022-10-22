from django.db import models

# Create your models here.

RELATIONSHIP_CHOICES = (
		('Immediate', 'Immediate'),
		('Distant', 'Distant'),
		('Friend', 'Friend'),
	)

class People(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)

	def __str__(self):
		return self.first_name