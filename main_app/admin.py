from django.contrib import admin
from .models import Fish, Exercise, Candy, Photo

# Register your models here.
admin.site.register(Fish)
admin.site.register(Exercise)
admin.site.register(Candy)
admin.site.register(Photo)