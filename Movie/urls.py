from django.urls import path
from . import views

urlpatterns = [
    path('insert',views.InsertEdit,name="insert"),
    path('edit/<int:pk>',views.InsertEdit,name="edit"),
    path('allmovies',views.AllMovies,name="allmovies")
]
