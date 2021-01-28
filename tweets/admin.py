from django.contrib import admin

# Register your models here.
from .models import Tweet, TweetLike

<<<<<<< HEAD

class TweetLikeAdmin(admin.TabularInline):
=======
class  TweetLikeAdmin(admin.TabularInline):
>>>>>>> bb8adc725cc29a5ab85a0d2219a704e0efe8bd24
    model = TweetLike

class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Tweet

admin.site.register(Tweet, TweetAdmin)


