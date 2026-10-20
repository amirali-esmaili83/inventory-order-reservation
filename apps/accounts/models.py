from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("customer", "Customer")
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10,
                            choices=ROLE_CHOICES,
                            default="customer",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]