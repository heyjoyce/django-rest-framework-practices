from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializer import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer