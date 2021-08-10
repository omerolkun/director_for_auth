from django.core.exceptions import RequestAborted
from django.shortcuts import render
from .models import Director
from .forms import YonetmenForm
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
    context = {
        'q':idid,
    }
    return render(request, 'app_d/detail.html',context)


def edit(request):
    form = YonetmenForm()
    context = {
        'form':form,
    }
    return render (request,'app_d/edit_director.html',context)