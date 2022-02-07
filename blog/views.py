from django.shortcuts import render
from .models import Post, Tag
# Create your views here.


def posts(request):
    tags = Tag.objects.all()
    lang = request.GET.get('lang', None)
    tag = request.GET.get('tag', None)
    if tag:
        # tag_id = Tag.objects.filter(name=tag).first().id
        print(Post.objects.filter(tags__in=[Tag.objects.filter(name=tag).first().id]).order_by('created_at').query)
        posts = Post.objects.filter(tags__in=[Tag.objects.filter(name=tag).first().id]).order_by('created_at')
    else:
        posts = Post.objects.all().order_by('created_at')
    return render(request, 'posts.html', {'posts': posts, 'lang': lang, 'tags': tags})


def post_detail(request, slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request, 'post_detail.html', {'post': post})
