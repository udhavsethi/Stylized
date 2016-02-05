from django.contrib import admin

# Register your models here.
from .models import Category, Style, Salon, StyleSalon, User, Transaction, StyleImage, SalonImage

admin.site.register(Category)
admin.site.register(Style)
admin.site.register(StyleImage)
admin.site.register(Salon)
admin.site.register(SalonImage)
admin.site.register(StyleSalon)
admin.site.register(User)
admin.site.register(Transaction)