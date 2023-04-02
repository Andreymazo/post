from django.core.management import BaseCommand

from users.models import CustomUser, Post, Comment


class Command(BaseCommand):

    def handle(self, *args, **options):
        a = Post.objects.all()
        b = CustomUser.objects.all()
        for i in a:#Smozhem zapolnit esli est posti
            # print(i.id)
            for ii in b.filter(id=i.id):#Chtobi lishnie perebori ne delat vstavlyaem id=i.id
                # print(ii.username)
                comment = Comment.objects.create(
                    comment_author=ii,#Chei comment
                    post=i,# K kakomu postu otnositsya
                    text='DataGrip is a database management environment for developers. It is designed to query, т'
                )
                comment.save()