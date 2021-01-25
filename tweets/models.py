from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL
# Create your models here.

class Tweet(models.Model):
    #SQL complecated
    #id = models.AutoField(primary_key=True)

    #many user many tweets 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id":self.id,
            "content":self.content,
            "likes":random.randint(100,1000)
        }  