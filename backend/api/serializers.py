from rest_framework import serializers

from api.models import Movie, User, MovieList, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']  

    
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=100, allow_blank=True)
    last_name = serializers.CharField(max_length=100, allow_blank=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

class MovieListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    def create(self, validated_data):
        movies = validated_data.pop('movies')
        movie_list = MovieList.objects.create(**validated_data)
        movie_list.movies.set(movies)
        return movie_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.movies.set(validated_data.get('movies'))
        instance.save()
        return instance
