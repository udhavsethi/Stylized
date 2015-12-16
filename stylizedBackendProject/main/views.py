from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("You have arrived at the stylized back-end index. || Coming Soon: Index for the various requests supported by the back-end engine. ||")