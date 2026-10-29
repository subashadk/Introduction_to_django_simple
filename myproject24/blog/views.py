from django.shortcuts import render
from .models import Post
from django.db.models import Q
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    query = request.GET.get('q')#search key words
    category = request.GET.get('category')#search by category firter

    #search useing Q
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    if category:
        posts = posts.filter(category__iexact=category)

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'query': query,
        'category': category,
        })
