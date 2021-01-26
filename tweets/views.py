
import random
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import redirect

from django.conf import settings
ALLOWED_HOSTS  = settings.ALLOWED_HOSTS 
from django.utils.http import is_safe_url

def home_view(request, *args, **kwargs):
    #print(args, kwargs)
    print(request.user or None)
    return render(request, "pages/home.html", context={}, status=200)
    
def tweet_create_view(request, *args, **kwargs):
    user = request.user

    if not request.user.is_authenticated:
        user = None  ## None for AnonymousUser
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    print("Ajax request:",request.is_ajax())
    form = TweetForm(request.POST or None)
    #print("Post data is:",request.POST)
    next_url = request.POST.get('next')
    
    if form.is_valid():
        obj = form.save(commit=False)
        # Do other form related logic
        obj.user = user 


        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201) # 201 for created items
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()

    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)

    return render(request,'components/form.html', context={"form": form})



def Tweet_LIstView (request, *args, **kwargs):
    qs = Tweet.objects.all()
    #tweets_list = [{"id":x.id, "content":x.content, "likes":random.randint(0,1000)} for x in qs]
    tweets_list = [x.serialize() for x in qs]
    
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