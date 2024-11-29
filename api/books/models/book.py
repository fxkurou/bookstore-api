from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    """
    Book model with title, author, description, publication date, price, stock, created at and updated at fields.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        description (str): The description of the book.
        publication_date (date): The publication date of the book.
        price (decimal): The price of the book.
        stock (int): The stock of the book.
        created_at (datetime): The created date of the book.
        updated_at (datetime): The updated date of the book.
    """

    title = models.CharField(_("title"), max_length=100)
    author = models.CharField(_("author"), max_length=100)
    description = models.TextField(_("description"))
    publication_date = models.DateField(_("publication date"))
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    stock = models.IntegerField(_("stock"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["created_at"]

    def __str__(self):
        return self.title + " - " + self.author + " - " + str(self.publication_date)
