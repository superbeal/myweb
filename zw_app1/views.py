#coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


def user_login(request):
    return render(request, 'zw_app1/login.html')


def login_in(request):
    """
    接收用户名和密码，与数据库中的数据比较，匹配成功就返回登录成功页面
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        redirect(reverse('zw_app1:login_success'))
    else:
        redirect(reverse('zw_app1:login'))


def login_success(request):
    """
    作为登录成功返回的页面

    """
    return HttpResponse("登录成功")




