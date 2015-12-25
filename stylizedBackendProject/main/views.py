from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.http import JsonResponse

from .models import Category
from main.serializers import CategorySerializer

# Create your views here.

def index(request):
	return HttpResponse("You have arrived at the stylized back-end index. || Coming Soon: Index for the various requests supported by the back-end engine. ||")

class CategoryIndexView(generics.ListAPIView):
	"""
	Returns a list of all categories
	"""
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


def salonIndex(request, location):
	salons = Salon.objects.filter(salon_location=location).order_by('avg_rating')

def styleIndex(request, category):
	styles = Style.objects.filter(category=category)	#TODO: Order the styles by trending or latest



#Dump:
# def categoryIndex(request):
# 	# categories = Category.objects.all()
# 	categories = Category.objects.get(pk=1)
# 	# returnn HttpResponse(categories)
# 	return JsonResponse({"category": "categories.cat_name"})