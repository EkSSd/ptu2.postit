from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.UserCreate.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/comments/', views.CommentList.as_view()),
    path('Comments/<int:pk>', views.CommentDetail.as_view()),
    path('posts/<int:pk>/like/', views.PostLikeCreate.as_view()),
]