from typing import Type
from django.db import models
from  embed_video.fields  import  EmbedVideoField
class Learning(models.Model):

    Title = models.CharField(max_length=100)
    Name_Ent_Med = models.CharField(max_length=100)
    Description =  models.TextField()
    Url = EmbedVideoField()
    Type = models.CharField(max_length=100)

    class  Meta:
    		verbose_name_plural = "Learning"

    def __str__(self):
        return str(self.Title)
