from django.contrib import admin
from userfeed.models import Post, UserProfile, Comment, Like
# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Like)

