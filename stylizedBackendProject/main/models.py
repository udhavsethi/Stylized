from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Category(models.Model): 
	cat_name = models.CharField(max_length=200)
	icon_img = models.ImageField(null=True)
	back_img = models.ImageField(null=True)
	def __str__(self):
		return self.cat_name

@python_2_unicode_compatible
class Style(models.Model):
	category = models.ForeignKey(Category)
	style_name = models.CharField(max_length=200)
	suitable_for = models.CharField(max_length=20)		#men/women/children
	description = models.TextField(blank=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	def __str__(self):
		return self.style_name

class StyleImage(models.Model):
	style = models.ForeignKey(Style, related_name='images')
	image = models.ImageField(null=True)
	def __str__(self):
		return str(self.image)

@python_2_unicode_compatible
class Salon(models.Model):
	salon_name = models.CharField(max_length=200)
	salon_location = models.CharField(max_length=200)
	salon_phone = models.CharField(max_length=200)								#can store multiple phone numbers
	salon_email = models.EmailField(blank=True)
	address = models.TextField()
	gmaps_url = models.URLField(blank=True)
	avg_rating = models.CharField(max_length=20, blank=True)
	style_menu = models.ManyToManyField(Style, through='StyleSalon')			#styles provided by the salon
	def __str__(self):
		return self.salon_name

class SalonImage(models.Model):
	salon = models.ForeignKey(Salon, related_name='images')
	image = models.ImageField(null=True)
	def __str__(self):
		return str(self.image)

@python_2_unicode_compatible
class StyleSalon(models.Model):
	style = models.ForeignKey(Style)
	salon = models.ForeignKey(Salon)
	ss_rating = models.CharField(max_length=20, blank=True)			#style-salon rating
	num_ratings = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=6, decimal_places=2, default="0.00")
	def __str__(self):
		return '%s | %s' % (self.style, self.salon)

@python_2_unicode_compatible
class User(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200, blank=True)
	user_phone = models.CharField(max_length=200)
	user_email = models.EmailField(blank=True)
	password = models.CharField(max_length=200)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	age = models.IntegerField(default=0, blank=True)
	user_location = models.CharField(max_length=200, blank=True)
	login_via = models.CharField(max_length=20)		#fb/insta/gmail
	bookmarks = models.ManyToManyField(Style,related_name='bookmarks+')
	likes = models.ManyToManyField(Style,related_name='likes+')
	history = models.ManyToManyField(StyleSalon, through='Transaction')		#All the style-salon pairs tried by the user
	user_img = models.ImageField(null=True)
	def __str__(self):
		return self.user_email

@python_2_unicode_compatible
class Transaction(models.Model):
	user = models.ForeignKey(User)
	style_salon = models.ForeignKey(StyleSalon)
	user_rating = models.CharField(max_length=20, blank=True)		#user-salon-style rating
	datetime = models.DateTimeField()
	price = models.DecimalField(max_digits=6, decimal_places=2, default="0.00")
	def __str__(self):
		return '%s | %s' % (self.user, self.style_salon)