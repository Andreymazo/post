import json
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from users.models import Post, Comment, CustomUser
from users.serializers import PostSerializer, CommentSerializer, CustomRegisterSerializer
from users.serializers import get_username_max_length
from users.serializers import CustomRegisterSerializer


class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterSerializer


class UserRegistration(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            get_username_max_length()
            serializer.save(request)
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Chtobi ne pisat quryset ...

    # def get_queryset(self): #Eto zhe realizovano v settings.py (strochki 72-74)
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
