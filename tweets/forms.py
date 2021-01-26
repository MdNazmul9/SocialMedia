from django import forms
from .models import Tweet

from django.conf import settings
TWEET_MAX_LENTG = settings.TWEET_MAX_LENTG

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > TWEET_MAX_LENTG:
            raise forms.ValidationError("This is too long")
        return content
        
    

         
      
