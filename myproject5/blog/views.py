from django.shortcuts import render
from datetime import datetime   

# Create your views here.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        'name': 'John Doe',
        'age': 25,
        "skills": ["Python", "Django", "JavaScript"],
        "user": User("Jane Smith", 30),
        "price": 19.99,
        "blog":{
            "title": "My First Blog Post",
            "author":{
                "name": "John Doe",
            },
            "content": "<b>This is the content of my first blog post.</b>",
            "created_at": datetime(2025, 1, 15, 10, 30)
        },
        "empty_value": None,
        }
    
    return render(request, 'blog/home.html', context)