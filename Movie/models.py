from django.db import models
# Create your models here.
class Actor(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Movie(models.Model):
    title=models.CharField(max_length=100)
    released_year=models.DateField()
    actors=models.ManyToManyField(Actor,related_name='actors')
    @property
    def display_actors(self):
        """Returns a comma-separated string of actor names."""
        return ", ".join([actor.name for actor in self.actors.all()])

    def __str__(self):
        return self.title