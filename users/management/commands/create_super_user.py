from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            username='andrey_mazo',
            age=10,
            number= 3245,
            date_of_birth='1985-04-02',
            is_superuser=True,
            is_staff=True
        )
        user.set_password('qwert123asd')
        user.save()