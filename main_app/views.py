from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Fish, Candy
from .forms import ExerciseForm

# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def fish_index(request):
  fishes = Fish.objects.filter(user=request.user)
  return render(request, 'fishes/index.html', { 'fishes': fishes })

@login_required
def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  candies_fish_doesnt_have = Candy.objects.exclude(id__in = fish.candies.all().values_list('id'))
  exercise_form = ExerciseForm()
  return render(request, 'fishes/detail.html', { 
    'fish': fish, 'exercise_form': exercise_form, 'candies': candies_fish_doesnt_have 
  })

@login_required
def add_exercise(request, fish_id):
  form = ExerciseForm(request.POST)
  if form.is_valid():
    new_exercise = form.save(commit=False)
    new_exercise.fish_id = fish_id
    new_exercise.save()
  return redirect('fish-detail', fish_id=fish_id)

@login_required
def assoc_candy(request, fish_id, candy_id):
  Fish.objects.get(id=fish_id).candies.add(candy_id)
  return redirect('fish-detail', fish_id=fish_id)

class FishCreate(LoginRequiredMixin, CreateView):
  model = Fish
  fields = ['name', 'species', 'description', 'age']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FishUpdate(LoginRequiredMixin, UpdateView):
  model = Fish
  fields = ['species', 'description', 'age']

class FishDelete(LoginRequiredMixin, DeleteView):
  model = Fish
  success_url = '/fishes/'

class CandyCreate(LoginRequiredMixin, CreateView):
  model = Candy
  fields = '__all__'

class CandyList(LoginRequiredMixin, ListView):
  model = Candy

class CandyDetail(LoginRequiredMixin, DetailView):
  model = Candy

class CandyUpdate(LoginRequiredMixin, UpdateView):
  model = Candy
  fields = ['name', 'color']

class CandyDelete(LoginRequiredMixin, DeleteView):
  model = Candy
  success_url = '/candies/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('fish-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)