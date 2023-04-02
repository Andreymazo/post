from django.core.management import BaseCommand

from users.models import CustomUser, Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        # usernames = ['testtest', 'foreig_papa', 'andrey_mazo']
        # for i in CustomUser.objects.all():
        #     print('-----------------', i.pk)
        # for i in usernames:
        for i in CustomUser.objects.all():
            post = Post.objects.create(
                post_author=i,
                title='Lebedi',
                text=f'Реализую для {i.username} авторизацию с регистрацией на django. Регистрация прошла успешна, но при попытке авторизоваться выходит'
            )
            post.save()
