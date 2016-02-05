from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from django.http import JsonResponse

from .models import Category, Style, Salon, User, StyleSalon, Transaction
from main.serializers import CategorySerializer, SalonSerializer, StyleSerializer, UserSerializer, StyleSalonSerializer

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
	serializer_class = StyleSalonSerializer

	def get_queryset(self):
		return StyleSalon.objects.filter(style=self.kwargs['pk'])
		# return StyleSalon.objects.filter(style=self.kwargs['pk']).select_related('salon')
		# return StyleSalon.objects.filter(salon__style_menu=self.kwargs['pk'])

class StyleForCategory(generics.ListAPIView):
	"""
	Returns a list of all styles for a category
	"""
	serializer_class = StyleSerializer

	def get_queryset(self):
		#expects names of categories appended with + sign for multiple filtering
		#TODO: Order the styles by trending or latest
		cat_list = (self.kwargs['cat_list']).split('+')
		print(cat_list)
		return Style.objects.filter(category__cat_name__in=cat_list)

class SalonDetail(generics.RetrieveAPIView):
	"""
	Returns all details for a single salon
	"""
	serializer_class = SalonSerializer

	def get_queryset(self):
		return Salon.objects.filter(pk=self.kwargs['pk'])
		# return get_object_or_404(Salon, pk=self.kwargs['pk'])

class StyleDetail(generics.RetrieveUpdateAPIView):
	"""
	Returns all details for a single styles
	"""
	serializer_class = StyleSerializer

	def get_queryset(self):
		return Style.objects.filter(pk=self.kwargs['pk'])

class UserDetail(generics.RetrieveUpdateAPIView):
	"""
	Returns details for profile view of the User
	"""
	serializer_class = UserSerializer

	def get_queryset(self):
		return User.objects.filter(pk=self.kwargs['pk'])


class UserIndex(generics.ListCreateAPIView):
	"""
	Returns a list of all users, allows creating, updating and deleting
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer