from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_details(request):
    post = {
        "title": "My second template Post",
        "description": "This is my second template post",
        "author": None,
        "created_at": datetime.now(),
        "comments_count": 5,
        "tags": ["django", "python", "web development"],
        "price": 19.99,
        "number": 42,
    }

    return render(request, 'blog/blog_details.html', {"post": post})