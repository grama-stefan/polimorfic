from django.contrib import admin

# Register your models here.


from . models import Post, Comment

    
    
admin.site.register(Post)    # a inregistrat Post

admin.site.register(Comment)          # a inregistrat Comment

