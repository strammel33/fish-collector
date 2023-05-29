from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('fishes/', views.fish_index, name='fish-index'),
  path('fishes/<int:fish_id>/', views.fish_detail, name='fish-detail'),
  path('fishes/create/', views.FishCreate.as_view(), name='fish-create'),
  path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fish-update'),
  path('fishes/<int:pk>/delete/', views.FishDelete.as_view(), name='fish-delete'),
  
]