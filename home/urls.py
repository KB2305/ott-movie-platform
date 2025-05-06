from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('movies', views.movies, name='movies'),
    path('register', views.register, name='register'),
    path('otp', views.otp, name='otp'),
    path('moviepage/<int:id>', views.moviepage, name='moviepage'),
    path('genre_list/<int:id>', views.genre_list, name='genre_list'),
    path('account', views.account, name='account'),  # fixed name
    path('watchlater', views.watch_later, name='watchlater'),
    path('ask_provide', views.ask_provide, name='ask_provide'),
    path('add_watch_later/', views.add_watch_later, name='add_watch_later'),
    path('ask_provide', views.ask_provide, name='ask_provide')
]
