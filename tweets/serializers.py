from django.conf import settings
from rest_framework import serializers
<<<<<<< HEAD
from profiles.serializers import PublicProfileSerializer
from .models import Tweet
=======
from .models import Tweet, TweetLike
>>>>>>> bb8adc725cc29a5ab85a0d2219a704e0efe8bd24

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS

<<<<<<< HEAD
class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip() # "Like " -> "like"
=======
TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS


class  TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField

    def validate_action(self, value):
        value = value.lower().strip() # "Like" --> "like"
>>>>>>> bb8adc725cc29a5ab85a0d2219a704e0efe8bd24
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for tweets")
        return value


<<<<<<< HEAD
class TweetCreateSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True) # serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['user', 'id', 'content', 'likes', 'timestamp']
    
    def get_likes(self, obj):
        return obj.likes.count()
    
=======

class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes']
    def get_likes(self, obj):
        return obj.likes.count()
        
>>>>>>> bb8adc725cc29a5ab85a0d2219a704e0efe8bd24
    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value

    # def get_user(self, obj):
    #     return obj.user.id


class TweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)
    class Meta:
        model = Tweet
        fields = [
                'user', 
                'id', 
                'content',
                'likes',
                'is_retweet',
                'parent',
                'timestamp']

    def get_likes(self, obj):
        return obj.likes.count()
