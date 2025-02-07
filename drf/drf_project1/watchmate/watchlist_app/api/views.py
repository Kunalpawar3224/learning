from django.shortcuts import render
from django.http import JsonResponse   
from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        movie_detail = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie_detail)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        movie_detail = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie_detail, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    if request.method == 'DELETE':
        movie_detail = Movie.objects.get(pk=pk)
        movie_detail.delete()
        return Response(status=204)
