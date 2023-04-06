from rest_framework.exceptions import ValidationError
import re
from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(**NULLABLE)
    number = models.IntegerField(**NULLABLE)
    date_of_birth = models.DateField(**NULLABLE)

    def __str__(self):
        return f"{self.username}, {self.is_staff}, {self.is_superuser}"


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    text = models.TextField(max_length=300, verbose_name='текст')
    image = models.ImageField(upload_to='media', **NULLABLE, verbose_name='изображение')
    post_author = models.ForeignKey('users.CustomUser', related_name='posts', on_delete=models.CASCADE,
                                    verbose_name='автор поста', **NULLABLE)  # 'auth,user'
    date_creation = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    date_lastreference = models.DateTimeField(auto_now_add=True, verbose_name='дата редактирования')

    def clean(self):
        print(self.post_author.age)
        if self.title == 'глупость':
            raise ValidationError('NNNo')
        if self.title == 'чепуха':
            raise ValidationError('NNNo')
        if self.title == 'ерунда':
            raise ValidationError('NNNo')
        if self.post_author.age < 18:  ##Vse rabotaet
            raise ValidationError('NNNo')

        return self.title

    def __str__(self):
        return f'{self.title}, {self.post_author}'


class Comment(models.Model):
    comment_author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name="comments",
                                       verbose_name='автор комментария', **NULLABLE)  #
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postsscomment',
                             verbose_name='к какому посту относится')
    text = models.TextField(max_length=300, verbose_name='текст')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    date_lastreference = models.DateTimeField(auto_now_add=True, verbose_name='дата редактирования')

    def __str__(self):
        return f'{self.comment_author}, {self.post} '
