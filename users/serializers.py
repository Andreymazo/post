import re
from allauth.account.adapter import get_adapter
from allauth.utils import get_username_max_length
from rest_framework import serializers, status
from users.models import Post, Comment, CustomUser
from rest_auth.registration.serializers import RegisterSerializer

NULLABLE = {'blank': True, 'null': True}
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'post_author', 'title', 'text', 'date_creation']


class CommentSerializer(serializers.ModelSerializer):
    # post_comment = PostSerializer(many=True, source='postsscomment')  #

    class Meta:
        model = Comment
        fields = ['id', 'comment_author', 'post', 'text']  # 'post_comment'


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(max_value=None, min_value=1)
    number = serializers.IntegerField()
    date_of_birth = serializers.DateField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'age', 'number', 'date_of_birth',)


    def get_cleaned_data(self):
        ss = re.search(r'mail\.ru', self.validated_data.get('email'))
        s = re.search(r'yandex\.ru', self.validated_data.get('email'))
        if s or ss == None:
            return serializers.ValidationError('No mail or yandex')
        return {
                'username': self.validated_data.get('username', ''),
                'password1': self.validated_data.get('password1', ''),
                'password2': self.validated_data.get('password2', ''),

                'email': self.validated_data.get('email', ''),

                'age': self.validated_data.get('age'),
                'number': self.validated_data.get('number'),
                'date_of_birth': self.validated_data.get('date_of_birth'),
            }


    # override save method of RegisterSerializer
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.age = self.cleaned_data.get('age')
        user.number = self.cleaned_data.get('number')
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.save()
        adapter.save_user(request, user, self)

        return user