from django.urls import path, include
# from rest_framework.routers import DefaultRouter


from backend.api.comment.api.views import CommentListCreateView

urlpatterns = [
    path('', CommentListCreateView.as_view(), name='comment-create'),

]
