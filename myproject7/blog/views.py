from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_list(request):
    blogs = [
        {
            "title": "django basics",
            "is_featured": True,
            "author": "subash"
        },
        {
            "title": "django advanced",
            "is_featured": False,
            "author": ""
        },
        {
            "title": "django best practices",
            "is_featured": False,
            "author": "ram"
        }
    ]

    context = {
        "blogs": blogs,
        "today": datetime.now(),
        "html_code": "<p>This is some HTML code.</p>"
    }

    return render(request, "blog/blog_list.html", context)