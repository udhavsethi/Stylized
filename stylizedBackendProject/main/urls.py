from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.CategoryIndexView.as_view(), name='categoryIndex'),
]