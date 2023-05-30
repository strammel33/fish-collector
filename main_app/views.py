from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish, Candy
from .forms import ExerciseForm

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
  exercise_form = ExerciseForm()
  return render(request, 'fishes/detail.html', { 
    'fish': fish, 'exercise_form': exercise_form })

def add_exercise(request, fish_id):
  form = ExerciseForm(request.POST)
  if form.is_valid():
    new_exercise = form.save(commit=False)
    new_exercise.fish_id = fish_id
    new_exercise.save()
  return redirect('fish-detail', fish_id=fish_id)

class FishCreate(CreateView):
  model = Fish
  fields = ['name', 'species', 'description', 'age']

class FishUpdate(UpdateView):
  model = Fish
  fields = ['species', 'description', 'age']

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fishes/'

class CandyCreate(CreateView):
  model = Candy
  fields = '__all__'

class CandyList(ListView):
  model = Candy

class CandyDetail(DetailView):
  model = Candy

class CandyUpdate(UpdateView):
  model = Candy
  fields = ['name', 'color']

class CandyDelete(DeleteView):
  model = Candy
  success_url = '/candies/'