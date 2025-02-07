from django.shortcuts import render
from django.http import JsonResponse   
from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
# Create your views here.

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    breakpoint()
    serializer = MovieSerializer(movies, many = True)
    # print(list(movies.values()))
    # data = {
    #     'movies': list(movies.values())
    # }

    return Response(serializer.data)

@api_view()
def movie_details(request, pk):
    movie_detail = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie_detail)
    print(movie_detail)
    # data = {
    #     'name': movie_detail.name,
    #     'description': movie_detail.descritory,
    #     'active_field': movie_detail.active_field
    # }
    return Response(serializer.data)