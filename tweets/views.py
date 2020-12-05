from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello world <h1>")

def home_Detail_view(request, tweet_id, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse(f"<h1>Hello {tweet_id} <h1>")