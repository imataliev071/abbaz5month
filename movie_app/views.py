from urllib import request

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer,
                          DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer)


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination

    def create(self, request):
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data=serializer.errors)
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'id': director.id}, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def director_list_api_view(request):
#     print(request.user)
#     directors = (Director.objects
#                  .prefetch_related('reviews')
#                  .select_related('movies').all())
#     if request.method == 'GET':
#         data = DirectorSerializer(directors, many=True).data
#         return Response(data=data)
#     if request.method == 'POST':
#         serializer = DirectorValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_404_NOT_FOUND,
#                             data=serializer.errors)
#         name = request.data.get('name')
#         director = Director.objects.create(name=name)
#         return Response(data={'id': director.id}, status=status.HTTP_201_CREATED)

class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        director = Director.objects.get(id=id)
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director.name = request.data['name']
        director.save()
        return Response(data={'message': 'Director updated'}, status=status.HTTP_200_OK)



# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, id):
#     director = Director.objects.get(id=id)
#     if request.method == 'GET':
#         try:
#             director = Director.objects.get(id=id)
#         except Director.DoesNotExist:
#             return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)
#         data = DirectorSerializer(director).data
#         return Response(data=data)
#     if request.method == 'PUT':
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         director.name = request.data['name']
#         director.save()
#         return Response(data={'message': 'Director updated'}, status=status.HTTP_200_OK)
#     if request.method == 'DELETE':
#         director.delete()
#         return Response('Director deleted', status=status.HTTP_200_OK)


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = (Movie.objects
                .select_related('director').all())
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data=serializer.errors)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration,
                                     director_id=director_id)

        return Response(data={'movies': movie.id}, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def movie_list_api_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data = MovieSerializer(movies, many=True).data
#         return Response(data=data)
#     if request.method == 'POST':
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_404_NOT_FOUND,
#                             data=serializer.errors)
#         title = request.data.get('title')
#         description = request.data.get('description')
#         duration = request.data.get('duration')
#         director_id = request.data.get('director_id')
#         movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
#     return Response(data={'movies': movie.id}, status=status.HTTP_201_CREATED)

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

    def update(self, queryset, *args, **kwargs):
        movie = Movie.objects.get(id=id)
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data={'movies': movie.id}, status=status.HTTP_200_OK)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, id):
#     movie = Movie.objects.get(id=id)
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response(data={'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         data = MovieSerializer(movie).data
#         return Response(data=data)
#     if request.method == 'PUT':
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         movie.title = request.data.get('title')
#         movie.description = request.data.get('description')
#         movie.duration = request.data.get('duration')
#         movie.director_id = request.data.get('director_id')
#         movie.save()
#         return Response(data={'movies': movie.id}, status=status.HTTP_200_OK)
#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')

        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data={'movie': review.id}, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         data = ReviewSerializer(reviews, many=True).data
#         return Response(data=data)
#
#     if request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         text = request.data.get('text')
#         movie_id = request.data.get('movie_id')
#         stars = request.data.get('stars')
#
#         review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
#         return Response(data={'movie': review.id}, status=status.HTTP_201_CREATED)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        reviews = Review.objects.get(id=id)
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reviews.text = request.data.get('text')
        reviews.movie_id = request.data.get('movie_id')
        reviews.save()
        return Response(data={'movie_id': reviews.id}, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     reviews = Review.objects.get(id=id)
#     if request.method == 'GET':
#         data = ReviewSerializer(reviews).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         reviews.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         reviews.text = request.data.get('text')
#         reviews.movie_id = request.data.get('movie_id')
#         reviews.save()
#         return Response(data={'movie_id': reviews.id}, status=status.HTTP_201_CREATED)

class MovieReviewListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
    pagination_class = PageNumberPagination

# @api_view(['GET'])
# def movie_review_list_api_view(request):
#     movies = Movie.objects.all()
#     data = MovieReviewSerializer(movies, many=True).data
#     return Response(data=data)
