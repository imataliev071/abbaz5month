from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/directors/', views.DirectorListCreateAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('api/v1/movies/', views.MovieListCreateAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewListCreateAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('api/v1/movies/reviews/', views.MovieReviewListAPIView.as_view()),
]
