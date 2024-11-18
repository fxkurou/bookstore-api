__all__ = ("BaseUserModel",)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.users.models import UserManager


class BaseUserModel(AbstractUser):
    """
    Base User model with email as the unique identifier
    The default that's used is "User"

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email of the user.
        phone (str): The phone number of the user.
    """

    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    email = models.EmailField(_("email"), unique=True)
    phone = models.CharField(_("phone"), max_length=15, blank=True)

    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    is_superuser = models.BooleanField(_("superuser status"), default=False)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
        ordering = ["-date_joined"]

    def save(self, *args, **kwargs):
        """
        Save the user with a hashed password.
        """
        if self.password and not self.password.startswith("pbkdf2_"):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
