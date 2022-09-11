from http.client import HTTPResponse
from operator import imod
from django.shortcuts import render 
from django.http import HttpResponse

def index(request):
  return render(request ,'index.html')
# Create your views here.
