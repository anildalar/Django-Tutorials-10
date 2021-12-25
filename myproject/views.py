
from django.shortcuts import render

def anil(response):
    #render(request, template_name, context=None, content_type=None, status=None, using=None)
    return render(response,'index.html')