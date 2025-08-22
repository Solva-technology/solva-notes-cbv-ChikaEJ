from django.db import models

from user.models import User


class Status(models.Model):
    name = models.TextField(verbose_name='Статус')
    is_final = models.BooleanField(verbose_name='Завершен', default=False)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Note(models.Model):
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=User,
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        verbose_name='Статус',
        to=Status,
        on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(
        verbose_name='Категории',
        to=Category,
        blank=True
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        permissions = [
            ("edit_any_note", "Can edit any note"),
        ]

    def __str__(self):
        return self.text
