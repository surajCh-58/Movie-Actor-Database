from django.contrib import admin
from .models import Actor, Movie
# Register your models here.
@admin.register(Actor)
class ActorsAdmin(admin.ModelAdmin):
    list_display=('id','name')

    search_fields=('name',)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display=('id','title','released_year')

    search_fields=('title',)