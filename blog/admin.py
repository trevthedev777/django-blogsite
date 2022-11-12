from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}  # fills slug field automatically  # noqa
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
 

# allows the admin to control the site backend
# admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']  # actions takes funcs as args

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
