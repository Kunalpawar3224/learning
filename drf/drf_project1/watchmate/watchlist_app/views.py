# from django.shortcuts import render
# from django.http import JsonResponse    
# from watchlist_app.models import Movie
# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     # print(list(movies.values()))
#     data = {
#         'movies': list(movies.values())
#     }

#     return JsonResponse(data)


# def movie_details(request, pk):
#     movie_detail = Movie.objects.get(pk=pk)
#     print(movie_detail)
#     data = {
#         'name': movie_detail.name,
#         'description': movie_detail.descritory,
#         'active_field': movie_detail.active_field
#     }
#     return JsonResponse(data)