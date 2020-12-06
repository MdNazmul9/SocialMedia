from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

def home_view(request, *args, **kwargs):
    #print(args, kwargs)
    return HttpResponse("<h1>Hello world <h1>")

def home_Detail_view(request, tweet_id, *args, **kwargs):
    #print(args, kwargs)
    '''

    REST API VIEW
    Consume by Javascript or Swift /java/iOS/Android
    return json data

    '''
    
    data = {

        "id": tweet_id,
      
    }

    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content

    except:
        #raise Http404
        data['meaasge'] = "Not Found"
        status = 404

    #return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content} <h1>")
    return JsonResponse(data , status=status)   # json.dumps content_type = 'application/json'