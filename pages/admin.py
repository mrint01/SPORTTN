from django.contrib import admin

from pages.models import UserInfo

class UserProfil(admin.ModelAdmin):
    list_display = ['user','address','phone']

admin.site.register(UserInfo, UserProfil)