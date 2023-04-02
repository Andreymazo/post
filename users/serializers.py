import re
from importlib.resources import _

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import get_username_max_length
from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response

from users.models import Post, Comment, CustomUser
from rest_auth.registration.serializers import RegisterSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'post_author', 'title', 'text', 'date_creation']


class CommentSerializer(serializers.ModelSerializer):
    # post_comment = PostSerializer(many=True, source='postsscomment')  #

    class Meta:
        model = Comment
        fields = ['id', 'comment_author', 'post', 'text']  # 'post_comment'


NULLABLE = {'blank': True, 'null': True}

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(max_value=None, min_value=1)
    number = serializers.IntegerField()
    date_of_birth = serializers.DateField()

    # def validate_email(self, email):###You must call `.is_valid()` before accessing `.validated_data`.
    #     email = get_adapter().clean_email(email)
    #     if re.search(r'yandex\.ru', self.validated_data.get('email')) == None:
    #         print('________________________________________________')
    #         raise serializers.ValidationError(
    #             _("Yandex or mail must be in e-mail address"))
    #     return email

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'age', 'number', 'date_of_birth',)




    # def get_cleaned_data(self):
    #     return {
    #         'username': self.validated_data.get('username', ''),
    #         'password1': self.validated_data.get('password1', ''),
    #         'password2': self.validated_data.get('password2', ''),
    #         'email': self.validated_data.get('email', ''),
    #         'age': self.validated_data.get('age'),
    #         'number': self.validated_data.get('number'),
    #         'date_of_birth': self.validated_data.get('date_of_birth'),
    #     }
    def get_cleaned_data(self):
        print('---------------', self.validated_data.get('email'))
        # if self.is_valid():
        #     return super().get_cleaned_data()  # Returns cleaned_data
        ss = re.search(r'mail\.ru', self.validated_data.get('email'))
        s = re.search(r'yandex\.ru', self.validated_data.get('email'))
        if s or ss == None:
            print('---------------', self.validated_data.get('email'))
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
# class UserSerializer(serializers.ModelSerializer):
#     # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
#     # comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
#     # lesson = LessonSerializer(source='smthin',  #####Komment 39,40,50 str chtobi update Course prohodil
#     # many=True)
#     ################################
#     # comment_author = CommentSerializer(many=True,
#     #                                    source="comments", allow_null=True)  # queryset=Comment.objects.all())#source='comment_author.username')
#     # post_author = PostSerializer(many=True,
#     #                              source='posts', allow_null=True)  # queryset=Post.objects.all())#source='post_author.username')
#     #########################################
#     class Meta:
#         model = get_user_model()
#         fields = ['username',
#                   'email',
#                   'password', ]  # 'comment_author', 'post_author' ##Dobavili dva castomnih polya-kluchi Useru,'comments','posts',
#
#
#     def create(self, validated_data):
#         #################################################3
#         # comment_data = validated_data.pop('comments')
#         # # print(lesson_data)
#         # smth = User.objects.create(**validated_data)
#         # for k in comment_data:
#         #     User.objects.create(smth=smth, **k)  ##Zdes course ne vidit
#         # return smth
#         #############################################
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password'],
#         )
#         return user
#
#
# # from django.utils.translation import gettext_lazy as _
# from rest_auth.registration.serializers import RegisterSerializer
#
# class CustomRegisterSerializer(RegisterSerializer):
#     any_additional_field_inserializer=serializers.CharField(
#         required=False,
#         max_length=2,
#     )
#     # username = serializers.CharField(
#     #     max_length=get_username_max_length(),
#     #     min_length=7,
#     #     required=True
#     # )
#
#     # username = serializers.CharField(
#     #     max_length=get_username_max_length(),
#     #     min_length=allauth_settings.USERNAME_MIN_LENGTH,
#     #     required=False
#     # )
#     # email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
#     # password1 = serializers.CharField(write_only=True)
#     # password2 = serializers.CharField(write_only=True)
#     #
#     # any_additional_field_inserializer = serializers.CharField(
#     #     required=False,
#     #     max_length=2,
#     # )
#
#     def get_cleaned_data(self):
#         data_dict = super().get_cleaned_data()
#         data_dict['any_additional_field_inserializer'] = self.validated_data.get('any_additional_field_inserializer', '')
#         return data_dict

    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     adapter.save_user(request, user, self)
    #     self.custom_signup(request, user)
    #     setup_user_email(request, user, [])
    #     return user
# class CurrentUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'id')
#
# from rest_framework import viewsets
#
# from users.models import User
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#     phone_numbers = ContactPhoneNumberSerializer(source='contactphonenumber_set', many=True)
#
#
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'first_name', 'last_name', 'date_of_birth',
#                    'phone_numbers', 'emails')
#
# user_list = UserViewSet.as_view({'get': 'list'})
# user_detail = UserViewSet.as_view({'get': 'retrieve'})
