from django.shortcuts import *
from . models import *
from . forms import *
# Create your views here.
def InsertEdit(request,pk=None):
    instance=get_object_or_404(Movie,id=pk) if pk else None
    if (request.method=="POST"):
        form=MovieForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("allmovies")
        else:
            form.add_error()
    else:
        form=MovieForm(instance=instance)
    return render(request,"InsertEdit.html",{'form':form})
def AllMovies(request):
    movie=Movie.objects.all()
    return render(request,"Allmovies.html",{'movies':movie})