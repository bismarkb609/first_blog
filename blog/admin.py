from django.contrib import admin
from .models import Post, UserAccount

# Register your models here.
admin.site.register(Post)
admin.site.register(UserAccount)