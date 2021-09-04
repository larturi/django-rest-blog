from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.api.permisions import isAdminOrReadOnly


class PostModelViewSet(ModelViewSet):
    permission_classes = [isAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
