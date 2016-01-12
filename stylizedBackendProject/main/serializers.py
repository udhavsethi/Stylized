from .models import Category, Style, Salon, User
from rest_framework import serializers

#TODO: Review all serializers to add fields/remove unwanted fields

class CategorySerializer(serializers.ModelSerializer):
	"""
	Serializing Categories
	"""
	class Meta:
		model = Category
		fields = ('cat_name',)

class SalonSerializer(serializers.ModelSerializer):
	"""
	Serializing Salons
	"""
	class Meta:
		model = Salon
		fields = ('salon_name', 'salon_location', 'salon_phone', 'salon_email', 'address', 'gmaps_url', 'avg_rating', 'style_menu')

class StyleSerializer(serializers.ModelSerializer):
	"""
	Serializing Styles
	"""
	class Meta:
		model = Style
		fields = ('category', 'style_name', 'suitable_for', 'description', 'views')

class UserSerializer(serializers.ModelSerializer):
	"""
	Serializing Users
	"""
	class Meta:
		model = User
		fields = ('firstname', 'lastname', 'user_phone', 'user_email', 'gender', 'age', 'user_location', 'login_via', 'bookmarks', 'likes','history')