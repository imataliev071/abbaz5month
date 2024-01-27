from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movie_count'.split()

    def get_movie_count(self, obj):
        return obj.movies.count()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title'.split()
        depth = 1


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration reviews average_rating'.split()

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0
