import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import User,Movie,Review,Genre
from api.serializers import UserSerializer,MovieSerializer,ReviewSerializer,GenreSerializer

@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail(request,pk=None):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist as e:
        return Response({"error" : str(e)})
    
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method in ["PUT", "PATCH"]:
        partial = (request.method == 'PATCH')
        serializer = MovieSerializer(instance=movie, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        movie.delete()
        return Response({"deleted" : True})
    
@api_view(["GET", "POST"])
def genre_list(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def genre_detail(request,pk=None):
    try:
        genre = Genre.objects.get(id=pk)
    except Genre.DoesNotExist as e:
        return Response({"error" : str(e)})
    
    if request.method == "GET":
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    elif request.method in ["PUT", "PATCH"]:
        partial = (request.method == 'PATCH')
        serializer = GenreSerializer(instance=genre, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        genre.delete()
        return Response({"deleted" : True})
