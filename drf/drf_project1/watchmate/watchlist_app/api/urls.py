from django.urls import path, include
from watchlist_app.api.views import WatchListView, WatchListDetailsView, \
                                    StreamPlatformView, StreamPlatformDetailView

urlpatterns = [
    path('list/', WatchListView.as_view(), name='movie_list'),
    path('<int:pk>', WatchListDetailsView.as_view(), name= 'movie_details'),

    path('platform-list/', StreamPlatformView.as_view(), name='streamPlatform_list'),
    path('platform/<int:pk>', StreamPlatformDetailView.as_view(), name= 'streamplatform-detail')
]
