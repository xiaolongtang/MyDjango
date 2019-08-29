# -*- coding: utf-8 -*-

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render_to_response
from django.shortcuts import render


# return a form page
def get_form(request):
    return render_to_response('form.html')


# handle the form
def submit(request):
    request.encoding = 'utf-8'
    if 'name' in request.GET:
        message = request.GET['name']
    else:
        message = 'Mr Empty'
    # return HttpResponse(message)
    context = {}
    context['message'] = message
    return render(request, 'index.html', context)

def hello(request):
    data = {
        'name': 'zhangsan',
        'age': 18,
    }
    return JsonResponse(data)