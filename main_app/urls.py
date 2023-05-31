from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('fishes/', views.fish_index, name='fish-index'),
  path('fishes/<int:fish_id>/', views.fish_detail, name='fish-detail'),
  path('fishes/create/', views.FishCreate.as_view(), name='fish-create'),
  path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fish-update'),
  path('fishes/<int:pk>/delete/', views.FishDelete.as_view(), name='fish-delete'),
  path('fishes/<int:fish_id>/add-exercise/', views.add_exercise, name='add-exercise'),
  path('fishes/<int:fish_id>/assoc-candy/<int:candy_id>', views.assoc_candy, name='assoc-candy'),
  path('candies/create/', views.CandyCreate.as_view(), name='candy-create'),
  path('candies/<int:pk>/', views.CandyDetail.as_view(), name='candy-detail'),
  path('candies/', views.CandyList.as_view(), name='candy-index'),
  path('candies/<int:pk>/update/', views.CandyUpdate.as_view(), name='candy-update'),
  path('candies/<int:pk>/delete/', views.CandyDelete.as_view(), name='candy-delete'),
  path('accounts/signup/', views.signup, name='signup')
]