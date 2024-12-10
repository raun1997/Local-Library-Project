from django.urls import reverse
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.timezone import now

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

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name="genre_name_case_insensitive_unique",
                violation_error_message="Genre already exists"
            ),
        ]

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    added_at = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books.
    # Author as a string rather than object because it hasn't been declared yet in file.

    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book"
    )
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    # Define a FileField with a subfolder named book_media/.
    # That’s where Django should store the images when you upload them.
    image = models.FileField(upload_to="book_media/", blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.pk)])

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.pk)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
