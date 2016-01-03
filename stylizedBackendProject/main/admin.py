from django.contrib import admin

# Register your models here.
from .models import Category, Style, Salon

admin.site.register(Category)
admin.site.register(Style)
admin.site.register(Salon)