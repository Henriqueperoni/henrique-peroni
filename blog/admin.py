from django.contrib import admin
from .models import Post, PostComment
# Register your models here.


class PostCommentAdminInline(admin.TabularInline):
    model = PostComment
    readonly_fields = ('user', 'post', 'comment', 'date_commented',)
    ordering = ('-date_commented',)


class PostAdmin(admin.ModelAdmin):
    inlines = (PostCommentAdminInline,)

    readonly_fields = ('post_date',)

    fields = ('author', 'title', 'slug',
              'title_tag', 'status', 'content',
              'image',)

    ordering = ('-post_date',)


admin.site.register(Post, PostAdmin)
