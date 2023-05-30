from django.db import models
from django.urls import reverse
from datetime import date

TIMES = (
  ('A', 'AM'),
  ('P', 'PM')
)

# Create your models here.
class Fish(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("fish-detail", kwargs={"fish_id": self.id})
  
  def exercised_today(self):
    return self.exercise_set.filter(date=date.today()).count() >= len(TIMES)

class Exercise(models.Model):
  date = models.DateField('Exercise date')
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )

  fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']