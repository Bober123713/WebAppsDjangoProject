from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('car', 'author', 'text', 'created_date')
    search_fields = ['car__make', 'car__model', 'author__username', 'text']
    list_filter = ('car', 'author', 'created_date')


# Register your models here
admin.site.register(Comment, CommentAdmin)
