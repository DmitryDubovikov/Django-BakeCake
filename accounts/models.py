from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = PhoneNumberField(verbose_name="Телефон", unique=True)

    # USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username} ({self.phone})"
