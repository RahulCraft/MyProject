from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#create a view
def index(request):
    return HttpResponse("<h1>Hello This is the first Django Project</h1>")
