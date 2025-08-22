from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name='Эл. почта', unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserProfile(models.Model):
    user = models.OneToOneField(
        verbose_name='Пользователь',
        to=User,
        on_delete=models.CASCADE
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return self.user.username
