from django.shortcuts import render
from .models import Fish

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  fishes = Fish.objects.all()
  return render(request, 'fishes/index.html', { 'fishes': fishes })

def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  return render(request, 'fishes/detail.html', { 'fish':fish })