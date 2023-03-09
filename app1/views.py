from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def yadav(request):
    return HttpResponse('<marquee><h1>yadav is a good boy</h1></marquee>')

def friends(request):
    return HttpResponse('<h1>friends are the medicine of happy life</h1>')
