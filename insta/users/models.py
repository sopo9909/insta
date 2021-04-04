from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
        ('C','Custom'),]
    """Default user for insta."""
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    profile_photo =models.ImageField(blank=True)
    website=models.URLField(blank=True, max_length=255)
    bio = models.TextField(blank=True)
    email=models.CharField(blank=True, max_length=255)
    phone_number=models.CharField(blank=True, max_length=255)
    gender=models.CharField(blank=True, max_length=255,choices=GENDER_CHOICES)
    followers=models.ManyToManyField('self')
    following=models.ManyToManyField('self')
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
