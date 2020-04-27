from django.db import models
# from django.conf import settings
from backend.api.product.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


class CommentManager(models.Manager):
    def all_comments(self):
        return super().all().filter(parent=None)

    def all_replies(self):
        return super().all().filter(parent__isnull=False)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

    def __str__(self):
        return 'comment by {} in {}'.format(self.user.username, self.product.name)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
