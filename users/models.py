from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}

# class User(models.Model):
#     login = models.TextField(max_length=25, verbose_name='логин')
#     password = models.Model(max_length=25, verbose_name='пароль')
#     number = models.IntegerField(verbose_name='номер')
#     date_birth = models.DateTimeField(verbose_name='дата рождения')
#     date_creation = models.DateTimeField(auto_now=True, verbose_name='дата создания')
#     date_lastreference = models.DateTimeField(auto_now_add=True, verbose_name='дата редактирования')
#
#     def __str__(self):
#         return f'{self.number}'

# class CustomUserManager(UserManager):
#
#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#
#         return self._create_user(email, password, **extra_fields)
#
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("The given email must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractUser):
#     # objects = CustomUserManager()
#     username = None
#     login = models.TextField(max_length=25, unique=True, verbose_name='логин')
#     # firstname = models.CharField(max_length = 60)
#     # lastname = models.CharField(max_length = 60)
#     email = models.EmailField(max_length=240, unique=True)
#     # phone = PhoneNumberField(null=True, blank=True)
#     # company =
#     password = models.CharField(max_length=24, unique=True)
#     number = models.IntegerField(verbose_name='номер')
#     # is_staff = models.BooleanField('staff status', default=False)
#     date_birth = models.DateTimeField(verbose_name='дата рождения')
#     date_creation = models.DateTimeField(auto_now=True, verbose_name='дата создания')
#     date_lastreference = models.DateTimeField(auto_now_add=True, verbose_name='дата редактирования')
#     USERNAME_FIELD = 'number'
#     REQUIRED_FIELDS = []  # 'firstname', 'lastname',
#
#
#     # user_permissions = None
#     # groups = None
#     def __str__(self):
#         return self.email
import re
from django.db import models
from django.contrib.auth.models import AbstractUser
import re
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(**NULLABLE)
    number = models.IntegerField(**NULLABLE)
    date_of_birth = models.DateField(**NULLABLE)
    def __str__(self):
        return f"{self.username}, {self.is_staff}, {self.is_superuser}"



    def clean_email(self):
        print('------------_______________')
        if re.search(r'mail\.ru',  f'{self.email}') != None:     ####'mail.ru' or 'yandex.ru' in self.email:
            print('------------_______________')
            return self.email
        print('_____________________err_______________')
        raise ValidationError('Only mail.ru, yandex.ru are permitted')


class Post(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='заголовок')
    text = models.TextField(max_length=300, verbose_name='текст')
    image = models.ImageField(upload_to='media', **NULLABLE, verbose_name='изображение')
    post_author = models.ForeignKey('users.CustomUser', related_name='posts', on_delete=models.CASCADE, verbose_name='автор поста', **NULLABLE) #'auth,user'
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
        if self.post_author.age < 18:##Vse rabotaet
            raise ValidationError('NNNo')

        return self.title


    def __str__(self):
        return f'{self.title}, {self.post_author}'

class Comment(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    comment_author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name="comments", verbose_name='автор комментария', **NULLABLE)#
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postsscomment', verbose_name='к какому посту относится')
    text = models.TextField(max_length=300, verbose_name='текст')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    date_lastreference = models.DateTimeField(auto_now_add=True, verbose_name='дата редактирования')

    def __str__(self):
         return f'{self.comment_author}, {self.post} '


