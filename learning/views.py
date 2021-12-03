from django.shortcuts import render
from .models import Learning
def fitness(request):
    vid = Learning.objects.all()
    context = {
	'vid': vid,
	}
    return render(request,"learning/entrainement/fitness.html",context )

def cardio(request):
    vid = Learning.objects.all()
    context = {
	'vid': vid,
	}
    return render(request,"learning/entrainement/cardio.html",context )    

def poitrine(request):
    vid = Learning.objects.all()
    context = {
	'vid': vid,
	}
    return render(request,"learning/entrainement/poitrine.html",context )     

def dorsau(request):
    vid = Learning.objects.all()
    context = {
	'vid': vid,
	}
    return render(request,"learning/entrainement/dorsau.html",context )  

def biceps(request):
    vid = Learning.objects.all()
    context = {
	'vid': vid,
	}
    return render(request,"learning/entrainement/biceps.html",context )  

def epaule(request):
    vid = Learning.objects.all()
    context = {
	'vid': vid,
	}
    return render(request,"learning/entrainement/epaule.html",context )  

def jambe(request):
    vid = Learning.objects.all()
    context = {
	'vid': vid,
	}
    return render(request,"learning/entrainement/jambe.html",context )  

def conseil_med(request):
    vid = Learning.objects.all()
    context = {
	'vid': vid,
	}
    return render(request,"learning/conseil_medical/conseil_med.html",context )  
# Create your views here.
