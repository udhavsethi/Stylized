from .models import Category, Style, Salon, User, StyleSalon, Transaction, Trending
from rest_framework import serializers

# from django.forms.models import model_to_dict

#TODO: Review all serializers to add fields/remove unwanted fields

class TrendingSerializer(serializers.ModelSerializer):
	"""
	Serializing trending Styles
	"""
	class Meta:
		model = Trending
		fields = ('style', 'tagline')


class CategorySerializer(serializers.ModelSerializer):
	"""
	Serializing Categories
	"""
	# trending = Trending.objects.all()
	trending = serializers.SerializerMethodField()

	def get_trending(self, obj):
		# trending_list = Trending.objects.all()
		# return TrendingSerializer(source=trending_list)
		return Trending.objects.values_list('style', 'tagline')

	class Meta:
		model = Category
		fields = ('id', 'cat_name', 'icon_img', 'back_img', 'trending')

class SalonSerializer(serializers.ModelSerializer):
	"""
	Serializing Salons
	"""
	images = serializers.StringRelatedField(many=True)
	class Meta:
		model = Salon
		fields = ('id', 'salon_name', 'salon_location', 'salon_phone', 'salon_email', 'address', 'gmaps_url', 'avg_rating', 'style_menu', 'images')

class StyleSerializer(serializers.ModelSerializer):
	"""
	Serializing Styles
	"""
	# id = serializers.ReadOnlyField()
	images = serializers.StringRelatedField(many=True)
	start_price = serializers.SerializerMethodField()
	related_styles = serializers.SerializerMethodField()

	def get_start_price(self, obj):
		return obj.salon_offers.values_list('price').order_by('-price')[1:]

	def get_related_styles(self, obj):
		return Style.objects.filter(category=obj.category, suitable_for=obj.suitable_for).exclude(id=obj.id).values()

	class Meta:
		model = Style
		fields = ('id', 'category', 'style_name', 'suitable_for', 'description', 'views', 'likes', 'images', 'start_price', 'related_styles')

class StyleSalonSerializer(serializers.ModelSerializer):
	"""
	Serializing Style-Salon pairs, containing salon detail as well as the ss-pair rating
	"""
	salon_detail = SalonSerializer(source='salon')
	# salon_detail = serializers.StringRelatedField(source='salon', read_only=True)
	class Meta:
		model = StyleSalon
		fields = ('ss_rating', 'num_ratings', 'price', 'style', 'salon_detail')

class TransactionSerializer(serializers.ModelSerializer):
	"""
	Serializing user-style-salon pairs representing the user transactions
	"""
	style_salon_detail = StyleSalonSerializer(source='style_salon')
	class Meta:
		model = Transaction
		fields = ('user_rating', 'user', 'style_salon_detail', 'datetime', 'price')

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
		fields = ('id', 'firstname', 'lastname', 'user_phone', 'user_email', 'gender', 'age', 'user_location', 'login_via', 'bookmarks_detail', 'likes_detail', 'history_detail', 'user_img')