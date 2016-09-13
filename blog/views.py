from django.shortcuts import render
from blog.models import Article, Tag, Classification, Picture
from django.http import JsonResponse
import math


def index(request):
    return render(request, 'index.html')


# 分页查询文章列表，默认每页10篇
def blog_list(request):
    try:
        page = int(request.GET['page'])
    except Exception:
        page = 1
    count = Article.objects.count()
    pagesize = 10
    blogs = Article.objects.all().order_by('-publish_time')[(page - 1) * pagesize:(page - 1) * pagesize+pagesize]
    totalpages = math.ceil(count/pagesize)
    tags = Tag.objects.all()
    classifications = Classification.objects.all()
    return render(request, 'blog.html', {
        "blogs": blogs,
        "total": count,
        "page": page,
        "totalPages": totalpages,
        "tags": tags,
        "classifications": classifications
    })


# 根据tag模糊查找文章
def search_by_tag(request):
    tagname=request.GET['tag']
    blogs1 = Article.objects.all()
    blogs=[]
    for blog in blogs1:
        if blog.tags.filter(tag_name__contains=tagname):
            blogs.append(blog)
    tags = Tag.objects.all()
    classifications = Classification.objects.all()
    return render(request, 'blog.html', {
        "blogs": blogs,
        "tags": tags,
        "classifications": classifications
    })


def search_by_classify(request):
    classify_name = request.GET['classify']
    blogs = Article.objects.filter(classification__name__contains=classify_name)
    tags = Tag.objects.all()
    classifications = Classification.objects.all()
    return render(request, 'blog.html', {
        "blogs": blogs,
        "tags": tags,
        "classifications": classifications
    })


def photo(request):
    try:
        page = int(request.GET['page'])
    except Exception:
        page = 1
    count = Picture.objects.count()
    pagesize = 8
    photos = Picture.objects.all()[(page - 1) * pagesize:(page - 1) * pagesize+pagesize]
    totalpages=math.ceil(count/pagesize)
    return render(request, 'photo.html', {
        "photos": photos,
        "total": count,
        "page": page,
        "totalPages": totalpages
    })


def full(request):
    id = request.GET['id']
    blog=""
    try:
        blog = Article.objects.get(id=id)
    except Exception:
        blog = Article.objects.first()
    tags = Tag.objects.all()
    classifications = Classification.objects.all()
    return render(request, 'full.html', {
        "blog": blog,
        "tags": tags,
        "classifications": classifications
    })


def aboutme(request):
    return render(request, 'aboutMe.html')






