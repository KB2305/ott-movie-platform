from django.shortcuts import get_object_or_404, redirect, render,HttpResponse

from ottProject import settings
from .models import UserDetail,Movies,Genre,Country,Language
from django.contrib import messages
from home import models
from django.core.mail import send_mail

import math
import random
import smtplib
# Create your views here.

 
# LOGIN PAGE
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if models.UserDetail.objects.filter(email = email).exists():
            return redirect('home')
        else:
            messages.success(request, "This Email id is not registered. Please Register first")
            return redirect('index')  # Redirect to a page where messages can be displayed

    return render(request, 'index.html')  


# REGISTRATION PAGE
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        request.session['email'] = email
        if not email:
            return HttpResponse("Error: no email found. Please register first.")
        otp = generate_otp()
        request.session['otp'] = otp  # Store OTP in session
        print("Generated OTP:", otp)  # Debugging line


        subject = 'Your otp code'
        msg = 'Your one time password is:' + otp
        from_email = settings.EMAIL_HOST_USER

        try:
            send_mail(subject, msg, from_email, [email])
            messages.success(request, "OTP sent successfully! Check your email.")
            return redirect('otp')
        
        except Exception as e:
            return HttpResponse(f"Error sending otp: {e}")
                
    return render(request, 'register.html')


# OTP GENERATION
def generate_otp():
    return ''.join(random.choices('1234567890',k=4))

def otp(request):
    print("Request method:", request.method)  # Debugging line

    if request.method == 'POST':
        otp = request.POST.get('otp')
        fix_otp = request.session.get('otp')
        email = request.session.get('email')

        if otp == fix_otp:
            del request.session['otp']  # Remove OTP after verification
            userdetail = UserDetail(email=email)
            userdetail.save()
            # del request.session['email']
            return redirect('home')
        else:
            return HttpResponse("Invalid OTP")

    return render(request, 'otp.html')


# HOME PAGE
def home(request):
    genre_list = models.Genre.objects.all()
    # genre_wise_data = []
    # for genre in genre_list:
    #     movie_genre = models.Movies.objects.filter(genre=genre)
    #     genre_wise_data.append({'genre': genre,'data':movie_genre})

    search = request.GET.get('search')
    if search:
        movies = models.Movies.objects.filter(name__icontains=search)
    else:
        movies = models.Movies.objects.all()

    history = []
    email = request.session.get('email')
    if email:
        user = UserDetail.objects.get(email=email)
        history = models.WatchHistory.objects.filter(user=user).order_by('-watched_on')[:6]

    # Fetching distinct languages from the Movies model
    language_list = models.Language.objects.all()
    language_wise_data = []

    # Group movies by language
    for language in language_list:
        movie = models.Movies.objects.filter(language=language)
        if movie.exists():
            language_wise_data.append({'language': language.name, 'data': movie})

    context = {'movies' : movies,
               'language_wise_data' : language_wise_data,
               'genre_list' : genre_list,
                'history': history
               }

    return render(request, 'home.html',context)

def movies(request):
    genre_list = models.Genre.objects.all()
   
    search = request.GET.get('search')
    if search:
        movies = models.Movies.objects.filter(name__icontains=search)
    else:
        movies = models.Movies.objects.all()

    # movies = models.Movies.objects.all()
    context = {
                'movies' : movies,
               'genre_list' : genre_list

    }
    return render(request, 'movies.html',context)

def moviepage(request,id):
    genre_list = Genre.objects.all()
    movie = Movies.objects.get(id=id)

    email = request.session.get('email')
    if email:
        user = UserDetail.objects.get(email=email)
        models.WatchHistory.objects.create(user=user, movie=movie)

    context = {'movies': movie, 'genre_list': genre_list}
    return render(request, 'moviepage.html', context)
    

def genre_list(request,id):
    genre_list = models.Genre.objects.all()
    genre = models.Genre.objects.get(id = id)
    movies = models.Movies.objects.filter(genre=genre)
    context = {
                'movies' : movies,
                'genre_list': genre_list

    }
    return render(request, 'genre_list.html',context)

def account(request):
    email = request.session.get('email')
    if not email:
        return redirect('index')
    user = UserDetail.objects.get(email=email)
    context = {'user': user}
    return render(request, 'account.html', context)

def watch_later(request):
    email = request.session.get('email')
    user = UserDetail.objects.get(email=email)
    items = models.WatchLater.objects.filter(user=user)
    return render(request, 'watch_later.html', {'items': items})

def add_watch_later(request):
    if request.method == 'POST':
        email = request.session.get('email')
        if not email:
            messages.error(request, "You must be logged in to add to Watch Later.")
            return redirect('index')

        try:
            user = UserDetail.objects.get(email=email)
        except UserDetail.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('index')

        movie_id = request.POST.get('movie_id')
        movie = Movies.objects.get(id=movie_id)

        if not models.WatchLater.objects.filter(user=user, movie=movie).exists():
            models.WatchLater.objects.create(user=user, movie=movie)

        return redirect('moviepage', id=movie_id)

    return redirect('home')

def ask_provide(request):
    if request.method == 'POST':
        movie_name = request.POST.get('movie_name')
        email = request.session.get('email')

        if not email or not movie_name:
            messages.error(request, "Please enter a movie name.")
            return redirect('ask_provide')

        try:
            user = UserDetail.objects.get(email=email)
            models.UserMovieRequest.objects.create(user=user, movie_name=movie_name)
            messages.success(request, "Your suggestion has been submitted!")
        except UserDetail.DoesNotExist:
            messages.error(request, "User not found.")

        return redirect('ask_provide')
    return render(request, 'ask_provide.html')

def logout_view(request):
    request.session.flush()
    return redirect('index')