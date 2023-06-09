# Generated by Django 4.1.7 on 2023-03-31 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('text', models.TextField(max_length=300, verbose_name='текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='изображение')),
                ('date_creation', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('date_lastreference', models.DateTimeField(auto_now_add=True, verbose_name='дата редактирования')),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор поста')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=200, verbose_name='к какому посту относится')),
                ('text', models.TextField(max_length=300, verbose_name='текст')),
                ('date_creation', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('date_lastreference', models.DateTimeField(auto_now_add=True, verbose_name='дата редактирования')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор комментария')),
            ],
        ),
    ]
