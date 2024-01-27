from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from rest_framework import status


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def test_api_view(request):
    json_object = {
        'int': 100,
        'float': 9.99,
        'text': 'hello',
        'dict': {
            'key': 'value'
        },
        'list': [1, 2, 3],
        'bool': True,
    }
    return Response(data=json_object)


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review).data
    return Response(data=data)


@api_view(['GET'])
def movie_review_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieReviewSerializer(movies, many=True).data
    return Response(data=data)
