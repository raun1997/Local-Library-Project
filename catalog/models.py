# reverse() is used in get_absolute_url() to get URL for specified ID
from django.urls import reverse

# using the django models
from django.db import models

# Constrains field to unique values
from django.db.models import UniqueConstraint

# Returns lower cased value of field
from django.db.models.functions import Lower

class Genre(models.Model):
	"""Model representation of a book genre."""
	name = models.CharField(
		max_length=200,
		unique=True,
		help_text="Enter a book genre"
	)

	def __str__(self):
		"""String for representing Model object."""
		return self.name

	def get_absolute_url(self):
		"""Returns the url to access a particular genre instance."""
		return reverse('genre-detail', args=[str(self.id)])

# class Meta:
# 	constraints = [
# 	UniqueConstraint(
# 		Lower('name'),
# 		name="genre_name_case_insensitive_unique")]
