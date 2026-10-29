from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_session(request):
    request.session['username'] = 'Adhik'
    request.session['course'] = 'Django'

    return HttpResponse(f"{request.session['username']} Session data is set")

def get_session(request):
    username =request.session.get('username', 'Guest')
    course = request.session.get('course', 'Not enrolled')
    return HttpResponse(f" wellcome: {username}, you are learning: {course}")

def delete_session(request):
    request.session.flush()#this will delete all session data
    return HttpResponse("Session data is deleted")
