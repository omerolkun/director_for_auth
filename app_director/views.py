from django.core.exceptions import RequestAborted
from django.shortcuts import render
from .models import Director,Movie
from .forms import FilmForm, FilmFormNoDirector, YonetmenForm
# Create your views here.

def home(request):
    context = {

    }
    return render (request, 'app_d/home.html',context)

def index(request):
    q = Director.objects.all()
    context = {
        'data':q,
    }
    return render (request, 'app_d/index.html',context)

def addDirector(request):
    if request.method == "POST":
        form = YonetmenForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
            form = YonetmenForm()
    context = {
        'form':form,
    }
    return render(request,'app_d/add_director.html',context)


def detail(request,idid):
    data = Director.objects.get(pk=idid)
    context = {
        'q':idid,
        'data':data,
    }
    return render(request, 'app_d/detail.html',context)


def edit(request,yonetmen_no):
    instance = Director.objects.get(pk=yonetmen_no)
    
    if request.method == 'POST':
        form = YonetmenForm(request.POST,instance=instance)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    else:
        form = YonetmenForm(instance=instance)

    form = YonetmenForm()
    context = {
        'form':form,
        'q':instance,
    }
    return render (request,'app_d/edit_director.html',context)

def deleteDirector(request,delete_id):
    q = Director.objects.get(pk=delete_id)
    x = Director.objects.get(pk=delete_id)
    
    x.delete()
    context = {
        'q':q,
    }
    return render (request,'app_d/delete.html',context)


def editMovie(request,m_id):

    instance = Movie.objects.get(pk=m_id)
    director_id = instance.dirco.pk
    if request.method == "POST":
        form1 = FilmForm(request.POST,instance=instance)
        if form1.is_valid:
            form1.save(commit=True)
            return detail(request,director_id)
    else:
        form1 = FilmForm(instance=instance)
    context = {
        'idko':m_id,
        'data':instance,
        'form':form1,
    }
    return render(request,'app_d/edit_movie.html',context)


def addMovie(request,drextor_id):
    x = Director.objects.get(pk=drextor_id)
    form1 = FilmFormNoDirector(request.POST or None)

    if request.method == 'POST':
        form1.dirco = x
        if form1.is_valid:
            form1.save(commit=True)
            return home(request)
    

    context = {
        'director':x,
        'fa':drextor_id,
        'form1':form1,
    }
    return render (request,'app_d/add_movie.html',context)