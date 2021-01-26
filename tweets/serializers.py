from django.conf import settings
from rest_framework import serializers
from .models import Tweet

TWEET_MAX_LENTG = settings.TWEET_MAX_LENTG

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']

    def validate_content(self, value):
        if len(value) > TWEET_MAX_LENTG:
            raise serializers.ValidationError("This tweet is too long")
        return value




