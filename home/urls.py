from lib2to3.pygram import pattern_symbols
from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name='index'),
    path("search/", views.search, name="search"),
    path("tv/<int:tv_id>/", views.view_tv_detail, name="tvDetail"),
    path("movie/<int:movie_id>/", views.view_movie_detail, name="movieDetail"),
    path("api/trending/", views.view_trending_tvShow, name="trending")
}
