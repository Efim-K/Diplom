from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """
    Модель Пользователя
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=30, verbose_name="Имя", **NULLABLE)
    last_name = models.CharField(max_length=30, verbose_name="Фамилия", **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", **NULLABLE)
    avatar = models.ImageField(upload_to="avatars/", verbose_name="Аватар", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
