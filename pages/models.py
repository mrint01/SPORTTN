from django.db import models
from django.contrib.auth.models import User



class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)


def __str__(self):
  return self.user.username
