from django.urls import path
from .views import movie_list, movie_detail, UserListCreateAPIView, UserDetailAPIView

urlpatterns = [
    path('movies/', movie_list),
    path('movies/<int:pk>/', movie_detail),

    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
]
