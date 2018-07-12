# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response


# 表单
def get_form(request):
    return render_to_response('form.html')


# 接收请求数据
def submit(request):
    request.encoding = 'utf-8'
    if 'name' in request.GET:
        message = 'you submit a name is ' + request.GET['name']
    else:
        message = 'you submit an empty form'
    return HttpResponse(message)