from django.contrib import admin
from .models import Learning
from  embed_video.admin  import  AdminVideoMixin
class  tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
    	pass
admin.site.register(Learning,tutorialAdmin)
# Register your models here.
