import json
import re

# from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response

from users.models import Post, Comment, CustomUser
from users.serializers import PostSerializer, CommentSerializer, CustomRegisterSerializer
# UserSerializer,

class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterSerializer


from users.serializers import get_username_max_length

from users.serializers import CustomRegisterSerializer

class UserRegistration(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterSerializer


    def post(self, request, *args, **kwargs):
        serializer = CustomRegisterSerializer(data=request.data)
        print('________________', request.data)
        if re.search(r'yandex\.ru', self.request.data['email']) == None:
            print('---------------', self.request.data['email'])
            return Response({'status':403, 'massage':'No yandex and mail prohibited'})
        if serializer.is_valid():
            get_username_max_length()
            # CustomRegisterSerializer.validate_email()
            # CustomRegisterSerializer.get_cleaned_data()
            print('---------------', self.request.data['email'])
            serializer.save(request)
            return Response(json, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # <---- INCLUDE REQUEST
        # if user:
        #     token = Token.objects.create(user=user)
        #     json = serializer.data
        #     json['token'] = token.key
        #     return Response(json, status=status.HTTP_201_CREATED)
        #
        # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserCreateView(APIView):
#
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save(request)  # <---- INCLUDE REQUEST
#             if user:
#                 token = Token.objects.create(user=user)
#                 json = serializer.data
#                 json['token'] = token.key
#                 return Response(json, status=status.HTTP_201_CREATED)
#
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]#Chtobi ne pisat quryset ...

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.is_active:
    #         return queryset.filter(is_staff=True)  ## Kazhdii mozhet smotret tolko svoi rassilki
    #     return queryset

    def perform_create(self, serializer):
        serializer.save(post_author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(comment_author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...

# def see_request(request):
#     text = f"""
#         Some attributes of the HttpRequest object:
#
#         scheme: {request.scheme}
#         path:   {request.path}
#         method: {request.method}
#         GET:    {request.GET}
#         user:   {request.user}
#     """
#
#     return HttpResponse(text, content_type="text/plain")


# def user_info(request):
#     text = f"""
#         Selected HttpRequest.user attributes:
#
#         username:     {request.user.username}
#         is_anonymous: {request.user.is_anonymous}
#         is_staff:     {request.user.is_staff}
#         is_superuser: {request.user.is_superuser}
#         is_active:    {request.user.is_active}
#     """
#
#     return HttpResponse(text, content_type="text/plain")

# from django.contrib.auth import logout
#
# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.
#
# from django.shortcuts import redirect
#
# def my_view2(request):
#     if not request.user.email.endswith('@yandex.com', '@mail.ru'):
#         return redirect('/login/?next=%s' % request.path)
#     # ...

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(user=self.request.user)
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated, AdminAuthenticationPermission,)
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from myapps.serializers import UserSerializer
# from rest_framework import viewsets
# from rest_framework.response import Response
#
# class UserViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
