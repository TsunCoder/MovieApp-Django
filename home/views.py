from email.policy import HTTP
from http.client import HTTPResponse
from django.shortcuts import render
import requests
from django.http import HttpResponse

from django.http.response import JsonResponse
# Create your views here.
API_KEY = "fed9e3d00c4d281e84b32381e1df8e69"


def search(request):
    # Get query from the search box
    query = request.GET.get('q')

    # If the query is not empty
    if query:
        # Get data from API
        data = requests.get(
            f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
    else:
        return HTTPResponse("Please enter a search query")
    return render(request, 'home/result.html', {
        "data": data.json(),
        "type": request.GET.get("type")
    })


def index(request):
    return render(request, 'home/index.html')


def view_tv_detail(request, tv_id):
    data = requests.get(
        f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={API_KEY}&language=en-US")
    recommendations = requests.get(
        f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations?api_key={API_KEY}&language=en-US")
    video = requests.get(
        f"https://api.themoviedb.org/3/movie/{tv_id}?api_key=fed9e3d00c4d281e84b32381e1df8e69&append_to_response=videos")

    return render(request, "home/tv_detail.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "video": video.json(),
        "type": "tv"
    })


def view_movie_detail(request, movie_id):
    data = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US")
    recommendations = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}&language=en-US")
    video = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=fed9e3d00c4d281e84b32381e1df8e69&append_to_response=videos")
    return render(request, "home/movie_detail.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "video": video.json(),
        "type": "movie"
    })


def view_trending_tvShow(request):
    trending = requests.get(
        f"https://api.themoviedb.org/3/trending/tv/week?api_key={API_KEY}&language=en-US")
    return JsonResponse(trending.json())
