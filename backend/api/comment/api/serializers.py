from rest_framework import serializers
from backend.api.comment.models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime
from backend.account.api.serializers import PublicUserSerilizer

# class ReplySerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField('username', read_only=True)
#     created_at = serializers.SerializerMethodField()

#     class Meta:
#         model = Comment
#         fields = '__all__'
#         # read_only_fields = ['replies']

#     def get_created_at(self, obj):
#         return naturaltime(obj.created_at)


class CommentSerializer(serializers.ModelSerializer):
    user = PublicUserSerilizer(read_only=True)
    created_at = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'product', 'created_at',
                  'content', 'replies', 'parent']

    def create(self, validate_data):
        user = self.context.get('request').user

        return Comment.objects.create(user=user, **validate_data)

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_replies(self, obj):
        """ self referral field """
        serializer = CommentSerializer(
            instance=obj.replies.all_replies(),
            many=True
        )
        return serializer.data
