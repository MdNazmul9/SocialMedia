from django import forms


from .models import Tweet

TWEET_MAX_LENTG = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > TWEET_MAX_LENTG:
            raise forms.ValidationError("This is too long")
        return content
        
    

         
      
