from django.utils.translation import gettext_lazy as _

from api.users.models.base import BaseUserModel


class User(BaseUserModel):
    """
    Custom User model with email as the unique identifier
    The default that's used is "User"

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email of the user.
        phone (str): The phone number of the user.
    """

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]
