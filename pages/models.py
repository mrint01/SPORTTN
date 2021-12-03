from django.db import models
from django.contrib.auth.models import User



class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email =   models.EmailField()
    address = models.CharField(max_length=250,null=True)
    phone = models.IntegerField(null=True)
    
    class Meta:
          verbose_name_plural = 'Profils'

    def __str__(self):
      return self.user.username

    
