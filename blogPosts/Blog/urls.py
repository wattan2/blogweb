from django.urls import path
from .views import PostDetailView, \
    PostCreateView, \
    PostUpdateView, \
    PostDeleteView, \
    PostListView, UserPostListView
from Users import views as user_views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/create', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]
