from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


# class PostAdmins(SummernoteModelAdmin):
#     summernote_fields = ('content',)

# admin.site.register(Post, PostAdmins)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','date_posted')
    search_fields = ['title', 'content']
    list_filter = ("author",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'email', 'body', 'active')
    list_filter = ("active",)
    search_fields = ['name', 'active']
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active = True)

admin.site.register(Comment, CommentAdmin)