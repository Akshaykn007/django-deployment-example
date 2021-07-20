from django.contrib import admin
from basic_app.models import UserProfileInfo
from .models import Video,Image,Documents

admin.site.register(UserProfileInfo)
admin.site.register(Video)
admin.site.register(Image)
admin.site.register(Documents)
