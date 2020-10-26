from django.shortcuts import render
from .models import Post
# Create your views here.
def all_article(request):
    all_article = Post.objects.all()
    context = {
        'posts':all_article,
    }
    return render(request,'all_article.html',context)

def article(request,id):
    article = Post.objects.get(id=id)
    context = {
        'post':article,
    }
    return render(request,'article.html',context)