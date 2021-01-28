import random
<<<<<<< HEAD
=======
from django.shortcuts import render, redirect
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.http import HttpResponse, Http404, JsonResponse

from .serializers import TweetSerializer, TweetActionSerializer
>>>>>>> bb8adc725cc29a5ab85a0d2219a704e0efe8bd24
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
<<<<<<< HEAD
    return render(request, "pages/feed.html")
=======
    #print(args, kwargs)
    #print(request.user or None)
    return render(request, "pages/home.html", context={}, status=200)


@api_view(['POST']) # http method the client== POST
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST)
    #print(serializer)
    if serializer.is_valid(raise_exception=True):
        obj = serializer.save(user=request.user)
        #print(obj)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['GET']) # http method the client== POST
def tweet_Detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)



@api_view(['DELETE', 'POST']) # http method the client== POST
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)

    if not qs.exists():
        return Response({"message":"You can't Delete this tweet!"}, status=401)
    
    qs = Tweet.objects.filter(user=request.user)
    obj = qs.first()
    obj.delete()
    return Response({"message":"Tweet removed successfully!"}, status=200)


@api_view(['POST']) # http method the client== POST
@permission_classes([IsAuthenticated])
def tweet_action_view(request, tweet_id, *args, **kwargs):
    '''
    id is required.
    Action options are like, unlike, rewrite
    '''
    print(request.POST, request.data)
    serializer = TweetActionSerializer(data=request.POST) 
    if serializer.is_valid(raise_exception=True):
        data = serializer.validate_data
        tweet_id = data.get("id")
        action = data.get("action")
        qs = Tweet.objects.filter(id=tweet_id)
        if not qs.exists():
            return Response({}, status=404)

        if not qs.exists():
            return Response({"message":"You can't Delete this tweet!"}, status=401)
        
        qs = Tweet.objects.filter(user=request.user)
        obj = qs.first()
        if action == "like":
             obj.likes.add(request.user)

             serializer = TweetSerializer(obj)
             return Response(serializer.data, status=200)
        elif action == "unlike":
             obj.likes.remove(request.user)

        elif action == "retweet":
             pass       

    return Response({"message":"Tweet removed successfully!"}, status=200)



@api_view(['GET']) # http method the client== POST
def Tweet_LIstView(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data)


def tweet_create_view_pure_django(request, *args, **kwargs):
    '''
    REST API Create View -> DRF
    ''' 
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



def Tweet_LIstView_pure_django(request, *args, **kwargs):
    qs = Tweet.objects.all()
    #tweets_list = [{"id":x.id, "content":x.content, "likes":random.randint(0,1000)} for x in qs]
    tweets_list = [x.serialize() for x in qs]
    
    data = {
        "isUser":False,
        "response": tweets_list
    }
    return JsonResponse(data)

def home_Detail_view_pure_django(request, tweet_id, *args, **kwargs):
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
>>>>>>> bb8adc725cc29a5ab85a0d2219a704e0efe8bd24

def tweets_list_view(request, *args, **kwargs):
    return render(request, "tweets/list.html")

def tweets_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, "tweets/detail.html", context={"tweet_id": tweet_id})
