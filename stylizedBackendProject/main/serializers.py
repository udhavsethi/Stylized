from .models import Category, Style, Salon, User, StyleSalon, Transaction
from rest_framework import serializers

#TODO: Review all serializers to add fields/remove unwanted fields

class CategorySerializer(serializers.ModelSerializer):
	"""
	Serializing Categories
	"""
	class Meta:
		model = Category
		fields = ('id', 'cat_name',)

class SalonSerializer(serializers.ModelSerializer):
	"""
	Serializing Salons
	"""
	class Meta:
		model = Salon
		fields = ('id', 'salon_name', 'salon_location', 'salon_phone', 'salon_email', 'address', 'gmaps_url', 'avg_rating', 'style_menu')

class StyleSerializer(serializers.ModelSerializer):
	"""
	Serializing Styles
	"""
	# id = serializers.ReadOnlyField()
	class Meta:
		model = Style
		fields = ('id', 'category', 'style_name', 'suitable_for', 'description', 'views')

class StyleSalonSerializer(serializers.ModelSerializer):
	"""
	Serializing Style-Salon pairs, containing salon detail as well as the ss-pair rating
	"""
	salon_detail = SalonSerializer(source='salon')
	# salon_detail = serializers.StringRelatedField(source='salon', read_only=True)
	class Meta:
		model = StyleSalon
		fields = ('ss_rating', 'style', 'salon_detail')

class TransactionSerializer(serializers.ModelSerializer):
	"""
	Serializing user-style-salon pairs representing the user transactions
	"""
	style_salon_detail = StyleSalonSerializer(source='style_salon')
	class Meta:
		model = Transaction
		fields = ('user_rating', 'user', 'style_salon_detail')

class UserSerializer(serializers.ModelSerializer):
	"""
	Serializing Users
	"""
	#TODO: include complete objects for style and history
	history_detail = TransactionSerializer(source='transaction_set', many=True)
	# history_detail = StyleSalonSerializer(source='history', many=True)
	bookmarks_detail = StyleSerializer(source='bookmarks', many=True)
	likes_detail = StyleSerializer(source='likes', many=True)
	class Meta:
		model = User
		fields = ('id', 'firstname', 'lastname', 'user_phone', 'user_email', 'gender', 'age', 'user_location', 'login_via', 'bookmarks_detail', 'likes_detail', 'history_detail')