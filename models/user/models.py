from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    """
    Custom User model
    """

    full_name = models.CharField(
        max_length=255, blank=True, null=True, help_text="Auto generated field"
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.first_name is not None and self.last_name is not None:
            self.full_name = (
                f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
            )
        else:
            self.full_name = ""
        super().save(*args, **kwargs)
