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
    form = YonetmenForm()
    context = {
        'q':form,
    }
    return render(request,'app_d/add_director.html',context)