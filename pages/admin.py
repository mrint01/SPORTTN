from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserInfo
from django.contrib.auth.models import User

# Register your models here.

class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = 'UserInfo'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserInfoInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)