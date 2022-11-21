from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# class PostAdmins(SummernoteModelAdmin):
#     summernote_fields = ('content',)

# admin.site.register(Post, PostAdmins)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','date_posted')
    search_fields = ['title', 'content']
    list_filter = ("author",)
    prepopulated_fields = {"slug": ("title",)}

    
    
    

admin.site.register(Post, PostAdmin)