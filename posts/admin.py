from django.contrib import admin
from .models import Post, Comment, UserProfile

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username')
    list_filter = ('author', 'created_at')
    ordering = ('-created_at',)
    
    
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at', 'approved')
    list_filter = ('approved', 'created_at', 'author')
    search_fields = ('content', 'author__username', 'post__title')
    actions = ['approve_comments', 'disapprove_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Mark selected comments as approved"
    
    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
    disapprove_comments.short_description = "Mark selected comments as disapproved"
    
    
admin.site.register(Comment, CommentAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')
    search_fields = ('user__username', 'user__email')
    
    
admin.site.register(UserProfile, UserProfileAdmin)
