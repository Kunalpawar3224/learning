from django.urls import path, include
from watchlist_app.api.views import MoviesListView, MovieDetailsView

urlpatterns = [
    path('list/', MoviesListView.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailsView.as_view(), name= 'movie_details')
]
