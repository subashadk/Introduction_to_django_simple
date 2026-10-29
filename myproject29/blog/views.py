from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def set_cookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('username', 'Subash', max_age=60*60*24  )  # Set cookie for 1 hour
    response.set_cookie('course', 'Django', max_age=60*60*24)  # Set cookie for 1 hour
    return response

def get_cookie(request):
    username = request.COOKIES.get('username')
    course = request.COOKIES.get('course')
    if 'username' in request.COOKIES:
      return HttpResponse(f"Cookie Value: {username}, Course: {course}")
    else:
      return HttpResponse("Cookie not found")

def delete_cookie(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response
