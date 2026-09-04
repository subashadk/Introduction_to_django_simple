from http.client import HTTPResponse

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the blog home.")

def about(request):
    return HttpResponse("Hello, world. You're at the about page.")

def post_detail(request, post_id):
    return HttpResponse(f"You're looking at post {post_id}.")

def user_profile(request, username):
    return HttpResponse(f"You're looking at the profile of  user {username}.")

# def article_archive(request, year, month):
#     return HttpResponse(f"You're looking at the archive for {month}/{year}.")

def article_detail(request, **kwargs):
    year = kwargs.get('year')
    month = kwargs.get('month')
    return HttpResponse(f"data {kwargs}")