
import random
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import redirect

def home_view(request, *args, **kwargs):
    #print(args, kwargs)
    return render(request, "pages/home.html", context={}, status=200)
    
def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    #print("Post data is:",request.POST)
    next_url = request.POST.get('next')
    print("Next url:", next_url)

    if form.is_valid():
        obj = form.save(commit=False)
        # Do other form related logic
        obj.save()
        

        if next_url != None:
            return redirect(next_url)

        form = TweetForm()

    return render(request,'components/form.html', context={"form": form})



def Tweet_LIstView (request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id":x.id, "content":x.content, "likes":random.randint(0,1000)} for x in qs]
    data = {
        "isUser":False,
        "response": tweets_list
    }


    return JsonResponse(data)






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