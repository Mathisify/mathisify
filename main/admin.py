from django.contrib import admin
from .models import Post, View

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

class ViewAdmin(admin.ModelAdmin):
    list_display = ('intpro', 'diginfo')


admin.site.register(Post, PostAdmin)
admin.site.register(View, ViewAdmin)
admin.site.site_header = "Mathisify Dashboard"
