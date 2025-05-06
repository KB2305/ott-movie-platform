from django.contrib import admin
from home import models

# Register your models here.
admin.site.register(models.UserDetail)
admin.site.register(models.Movies)
admin.site.register(models.Genre)
admin.site.register(models.Country)
admin.site.register(models.Language)
admin.site.register(models.WatchLater)
admin.site.register(models.UserMovieRequest)