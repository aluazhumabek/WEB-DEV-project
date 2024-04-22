from django.urls import path
from api.views import (
    UserDetailAPIView, UserListCreateAPIView,
    ReviewDetailAPIView, ReviewListCreateAPIView,
    movie_list, movie_detail,
    genre_list, genre_detail,
)

urlpatterns = [
    path('movies/', movie_list),
    path('movies/<int:pk>/', movie_detail),

    path('genres/', genre_list),
    path('genres/<int:pk>/', genre_detail),

    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),

    path('reviews/', ReviewListCreateAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
]
