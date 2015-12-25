from .models import Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
	"""
	Serializing Categories
	"""
	class Meta:
		model = Category
		fields = ('cat_name',)