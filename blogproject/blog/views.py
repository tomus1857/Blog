from django.shortcuts import render, HttpResponse
from .models import Post



def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def home (request):
    posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/home.html', {'posts':posts})