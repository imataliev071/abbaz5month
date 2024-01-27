from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer
from rest_framework import status


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    director = Director.objects.get(id=id)
    if request.method == 'GET':
        try:
            director = Director.objects.get(id=id)
        except Director.DoesNotExist:
            return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
        data = DirectorSerializer(director).data
        return Response(data=data)
    if request.method == 'PUT':
        director.name = request.data['name']
        director.save()
        return Response(data={'message': 'Director updated'}, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        director.delete()
        return Response('Director deleted', status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    directors = Director.objects.all()
    if request.method == 'GET':
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    if request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'id': director.id}, status=status.HTTP_201_CREATED)


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


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    if request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
    return Response(data={'movies': movie.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response(data={'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        data = MovieSerializer(movie).data
        return Response(data=data)
    if request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data={'movies': movie.id}, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)

    if request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')

        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data={'movie': review.id}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    reviews = Review.objects.get(id=id)
    if request.method == 'GET':
        data = ReviewSerializer(reviews).data
        return Response(data=data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.movie_id = request.data.get('movie_id')
        reviews.save()
        return Response(data={'movie_id': reviews.id}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_review_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieReviewSerializer(movies, many=True).data
    return Response(data=data)
