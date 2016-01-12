from django.contrib import admin

# Register your models here.
from .models import Category, Style, Salon, StyleSalon, User

admin.site.register(Category)
admin.site.register(Style)
admin.site.register(Salon)
admin.site.register(StyleSalon)
admin.site.register(User)