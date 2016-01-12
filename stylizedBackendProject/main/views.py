from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from django.http import JsonResponse

from .models import Category, Style, Salon, User
from main.serializers import CategorySerializer, SalonSerializer, StyleSerializer, UserSerializer

# Create your views here.

def index(request):
	return HttpResponse("You have arrived at the stylized back-end index. || Coming Soon: Index for the various requests supported by the back-end engine. ||")

class CategoryIndex(generics.ListAPIView):
	"""
	Returns a list of all categories
	"""
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class SalonForLocation(generics.ListAPIView):
	"""
	Returns a list of all salons for a given location in order of their rating
	"""
	serializer_class = SalonSerializer
	
	def get_queryset(self):
		return Salon.objects.filter(salon_location=self.args[0]).order_by('avg_rating')

class SalonForStyle(generics.ListAPIView):
	"""
	Returns a list of all salons that offer a style X
	"""
	serializer_class = SalonSerializer

	def get_queryset(self):
		return Salon.objects.filter(style_menu=self.kwargs['pk'])

class StyleForCategory(generics.ListAPIView):
	"""
	Returns a list of all styles for a category
	"""
	serializer_class = StyleSerializer

	def get_queryset(self):
		return Style.objects.filter(category__cat_name=self.args[0])	#TODO: Order the styles by trending or latest

class SalonDetail(generics.RetrieveAPIView):
	"""
	Returns all details for a single salon
	"""
	serializer_class = SalonSerializer

	def get_queryset(self):
		return Salon.objects.filter(pk=self.kwargs['pk'])
		# return get_object_or_404(Salon, pk=self.kwargs['pk'])

class StyleDetail(generics.RetrieveAPIView):
	"""
	Returns all details for a single styles
	"""
	serializer_class = StyleSerializer

	def get_queryset(self):
		return Style.objects.filter(pk=self.kwargs['pk'])

class UserDetail(generics.RetrieveAPIView):
	"""
	Returns details for profile view of the User
	"""
	serializer_class = UserSerializer

	def get_queryset(self):
		return User.objects.filter(pk=self.kwargs['pk'])