from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    username_validator = RegexValidator(
        regex=r'^[\w ]+$',  # Allows letters, numbers, and spaces
        message="Username can only contain letters, numbers, and spaces."
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
