from django.contrib import admin

# Register your models here.
from .models import owners, pets, appointments, vaccines, doctors

admin.site.register(owners)
admin.site.register(pets)
admin.site.register(doctors)