import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import User,Movie,MovieList,Review
from api.serializers import UserSerializer,MovieSerializer,MovieListSerializer,ReviewSerializer

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
    
