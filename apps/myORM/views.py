from django.shortcuts import render, redirect
from .models import Blog, Comment

# Create your views here.

def index(request):
    context = {
    'blogs': Blog.objects.all()
    # Select * FROM Blog
    }
    return render(request, 'myORM/index.html', context)

def blogs(request):
    # using ORM now
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    #Insert into Blog (title, blog, created_at, updated_at) values(title, blog, now(), now())
    return redirect('/')

def comments(request, id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog_id=blog)
    return redirect ('/')
