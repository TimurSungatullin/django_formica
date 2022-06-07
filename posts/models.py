from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=128, verbose_name='Название')

    text = models.TextField(verbose_name='Текс')

    def __str__(self):
        return f'{self.id}: {self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
