from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        usernames = ['testtest', 'foreig_papa']
        for i in usernames:
            user = CustomUser.objects.create(
                username=i,
                age=15,
                date_of_birth='1980-03-01',
                is_superuser=False,
                is_staff=True
            )
            user.set_password('qwert123asd')
            user.save()
