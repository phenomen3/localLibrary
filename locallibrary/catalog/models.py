from django.db import models

# Create your models here.

# Genre model
class Genre(models.Model):
    """Model representing a book genre."""
    # Field = column -- my_field_name -- strings of alpahanumeric characters
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    # Standar method
    def __str__(self):
        """String for representing the Model object."""
        return self.name

