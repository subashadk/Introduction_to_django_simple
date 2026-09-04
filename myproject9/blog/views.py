from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request):
    students_list = [
        {"name": "rahul", "class": "10th", "rollno": 1},
        {"name": "priya", "class": "10th", "rollno": 2},
        {"name": "sachin", "class": "10th", "rollno": 3},
    ]

    return render(request, 'blog/blog.html', {'students': students_list})
