from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.CategoryIndex.as_view(), name='categoryIndex'),
	url(r'^salons/([\w-]+)/$',views.SalonForLocation.as_view(), name='salonIndex'),
	url(r'^styles/([\w-]+)/$',views.StyleForCategory.as_view(), name='styleIndex'),
	url(r'^salon/(?P<pk>[0-9]+)/$',views.SalonDetail.as_view(), name='salonDetail'),
]