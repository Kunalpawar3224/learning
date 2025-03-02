from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status, generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from watchlist_app.api.permissions import IsAdminOrReadOnly, IsReviewUserorReadOnly
from watchlist_app.models import Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import WatchlistSerializer, StreamPlatFormSerializer, ReviewSerializer

class ReviewlistView(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(Watchlist=pk)
    
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(Watchlist=watchlist, review_user=review_user)

        # Check if user has already reviewed the movie before
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")
        
        if watchlist.number_ratings == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else: 
            watchlist.avg_rating = ((watchlist.avg_rating + serializer.validated_data['rating'])/2)

        watchlist.number_ratings = watchlist.number_ratings + 1
        watchlist.save()

        serializer.save(Watchlist=watchlist, review_user=review_user)  

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserorReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

class StreamPlatformView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatFormSerializer

# class StreamPlatformView(APIView):

#     def get(self, request):
#         StreamPlatforms = StreamPlatform.objects.all()
#         serializer = StreamPlatFormSerializer(StreamPlatforms, many = True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StreamPlatFormSerializer(data=request.data, context={'request': request} )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.data)
        
class StreamPlatformDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
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
    permission_classes = [IsAdminOrReadOnly]

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
    permission_classes = [IsAdminOrReadOnly]

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
