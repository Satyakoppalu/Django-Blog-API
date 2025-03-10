from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
