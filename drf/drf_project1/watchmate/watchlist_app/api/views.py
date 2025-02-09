from django.shortcuts import render
from django.http import JsonResponse   
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from watchlist_app.models import Watchlist, StreamPlatform
from watchlist_app.api.serializers import WatchlistSerializer, StreamPlatFormSerializer

class StreamPlatformView(APIView):

    def get(self, request):
        StreamPlatforms = StreamPlatform.objects.all()
        serializer = StreamPlatFormSerializer(StreamPlatforms, many = True, context={'request': request})
        lookup_field = 'slug'
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
        
class StreamPlatformDetailView(APIView):

    def get(self, request, pk):
        try:
            platform_detail = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "Platform does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StreamPlatFormSerializer(platform_detail, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform_detail = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatFormSerializer(platform_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        platform_detail = StreamPlatform.objects.get(pk=pk)
        platform_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class WatchListView(APIView):

    def get(self, request):
        movies = Watchlist.objects.all()
        serializer = WatchlistSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListDetailsView(APIView):

    def get(self, request, pk):
        try:
            movie_detail = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(movie_detail)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie_detail = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie_detail, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie_detail = Watchlist.objects.get(pk=pk)
        movie_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many = True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie_detail = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie_detail)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie_detail = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie_detail, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         movie_detail = Movie.objects.get(pk=pk)
#         movie_detail.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
