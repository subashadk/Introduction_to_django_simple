from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to my blog home</h1>")
def about(request):
    return HttpResponse("blog  about page")