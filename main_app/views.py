from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Add the Cat class & list and view function below the imports
class Fish:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

fishes = [
  Fish('Bubbles', 'guppy', 'Kinda rude.', 3),
  Fish('Silver', 'tuna', 'Looks like a turtle.', 0),
  Fish('CheezeIt', 'goldfish', 'likes cheese', 4),
  Fish('Mr. Pickles', 'barracuda', 'eats everyone else', 6)
]


def home(request):
  return HttpResponse('<h1>hello fishies</h1>')

def about(request):
  return render(request, 'about.html')

def fish_index(request):
  return render(request, 'fishes/index.html', { 'fishes': fishes})