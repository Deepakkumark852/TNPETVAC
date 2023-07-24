from django.contrib import admin

# Register your models here.
from .models import owners, pets, appointments, vaccines

admin.site.register(owners)
admin.site.register(pets)