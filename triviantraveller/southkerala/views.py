from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from . import forms
from southkerala.models import Blog,Comments,Hotels,Image
from .models import *

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    blog = Blog.objects.all().order_by('-blog_id')
    return render(request,"index.html",{'access_index':blog})
def about(request):
    return render(request,"about.html")
def destinations(request):
    return render(request,"destinations.html")

def blog(request):
    blog = Blog.objects.all().order_by('-blog_id')
    img = Image.objects.all()
    return render(request,"blog.html",{'access_records':blog,'access_img':img})

def blogdetail(request):
    imgli = []
    hotelli =[]
    commli = []
    if request.method =='POST':
        blog_id = request.POST.get("blog_id")
        blog = Blog.objects.get(blog_id=blog_id)
        img = Image.objects.all()
        hotel = Hotels.objects.all()
        comm = Comments.objects.all()
        for i in img:
            if (i.blog_id == blog):
                imgli.append(i)
        for j in hotel:
            if (j.blog_id == blog):
                hotelli.append(j)
        for k in comm:
            if (k.blog_id == blog):
                commli.append(k)


    return render(request,"blogdetail.html",{'access_blog':blog,'access_imgli':imgli,'access_hotli':hotelli,'access_com':commli})

def comments(request):
    imgli = []
    hotelli =[]
    commli = []
    if request.method =='POST':
        blog_id = request.POST.get("blog_id")
        blog = Blog.objects.get(blog_id=blog_id)
        img = Image.objects.all()
        hotel = Hotels.objects.all()
        com = Comments.objects.all()
        for i in img:
            if (i.blog_id == blog):
                imgli.append(i)
        for j in hotel:
            if (j.blog_id == blog):
                hotelli.append(j)
        for k in com:
            if (k.blog_id == blog):
                commli.append(k)
        #blog_id = request.POST.get("blog_id")
        name = request.POST.get("name")
        email_id = request.POST.get("email")
        comment = request.POST.get("comment")
        blog = Blog.objects.get(blog_id=blog_id)
        comm = Comments()
        comm.blog_id = blog
        comm.name = name
        comm.email_id = email_id
        comm.comment = comment
        comm.date =  date.today()
        comm.save()
    return render(request,"blogdetail.html",{'access_blog':blog,'access_imgli':imgli,'access_hotli':hotelli,'access_com':commli})

def destinations(request):
    blog = Blog.objects.all()
    return render(request,"destinations.html",{'access_index':blog})

def tips(request):
    return render(request,"tips.html")

def suggesions(request):
    if request.method =='POST':
        name = request.POST.get("name")
        suggesion = request.POST.get("suggesion")

        sugg = Suggesions()
        sugg.name = name
        sugg.suggesion = suggesion
        sugg.save()


    return render(request,"contact.html")
