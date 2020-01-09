from django.contrib import admin
from .models import Post #import posts


admin.site.register(Post) #register posts with admin page
