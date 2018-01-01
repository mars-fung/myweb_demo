from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from blog.models import Blog


def index(request):
    bolg_list = Blog.objects.all()
    return  render_to_response('index.html', {'blogs': bolg_list})

def base(request):
    bolg_list = Blog.objects.all()
    return  render_to_response('base.html', {'blogs': bolg_list})

def blog(request):
    return  render_to_response('blog.html')

def newblog(request):
    bolg_list = Blog.objects.all()
    return  render_to_response('newblog.html',{'blogs': bolg_list})

def login(request):
    return  render_to_response('login.html')

def login_action(request):
    if request.method == 'POST' or request.method == 'post':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin':
            return HttpResponse("Login Success!!!")
        else:
            # return render_to_response('login.html',{'error':'账号或密码错误'})
            return render(request,'login.html',{'error':'账号或密码错误'})
    else:
         return  HttpResponse("Not POST")
