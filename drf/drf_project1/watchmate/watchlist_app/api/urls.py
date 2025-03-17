from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (WatchListView, WatchListDetailsView,
                                    StreamPlatformView, ReviewlistView,
                                    ReviewDetailView, ReviewCreateView, UserReview)
# router is used when you are working with viewsets in Django REST framework, and it helps generate the URL 
# patterns for API endpoints automatically.
router = DefaultRouter()
router.register('platform', StreamPlatformView, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListView.as_view(), name='movie_list'),
    path('<int:pk>/', WatchListDetailsView.as_view(), name= 'movie_details'),

    path('', include(router.urls)),
    # path('platform-list/', StreamPlatformView.as_view(), name='streamPlatform_list'),
    # path('platform/<int:pk>', StreamPlatformDetailView.as_view(), name= 'streamplatform-detail'),

    # path('review/', ReviewlistView.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetailView.as_view(), name='review'),

    path('<int:pk>/review-create/', ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewlistView.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),

    path('reviews/', UserReview.as_view(), name='user-review-detail')
]
