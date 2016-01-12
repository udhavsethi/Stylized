from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.CategoryIndex.as_view(), name='categoryIndex'),
	url(r'^salonsforlocation/([\w-]+)/$',views.SalonForLocation.as_view(), name='salonForLocation'),
	url(r'^salonsforstyle/(?P<pk>[0-9]+)/$',views.SalonForStyle.as_view(), name='salonForStyle'),
	url(r'^styles/([\w-]+)/$',views.StyleForCategory.as_view(), name='styleIndex'),
	url(r'^salon/(?P<pk>[0-9]+)/$',views.SalonDetail.as_view(), name='salonDetail'),
	url(r'^style/(?P<pk>[0-9]+)/$',views.StyleDetail.as_view(), name='styleDetail'),
	url(r'^user/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(), name='userDetail'),
]