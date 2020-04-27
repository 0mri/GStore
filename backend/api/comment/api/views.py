from rest_framework import generics
from .serializers import CommentSerializer
from backend.api.comment.models import Comment


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # queryset = Comment.objects.all().filter(parent=None)
