from django.db import models

# Create your models here.

class UserDetail(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    def __str__(self):
        return "%s" % str(self.email)+'---->'+ str(self.id)

class Genre(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=35,null=True,blank=True)
    seq = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return "%s" % str(self.name)

class Language(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    def __str__(self):
        return "%s" % str(self.name)

class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    def __str__(self):
        return "%s" % str(self.name)

class  Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True,blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,null=True,blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE,null=True,blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True)
    year_of_release = models.DateField(null=True, blank = True)
    duration = models.DurationField(null=True, blank=True)
    path = models.TextField(null=True, blank=True)
    poster = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    cast = models.TextField(null=True, blank=True)
    director = models.TextField(null=True, blank=True)
    def __str__(self):
        return "%s" % str(self.name)

class WatchLater(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

class WatchHistory(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    watched_on = models.DateTimeField(auto_now_add=True)

class UserMovieRequest(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_name} by {self.user.email}"
