from django.contrib import admin
from .models import BlogPost , Comment
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('id','title','is_published','created_at')
	list_display_links = ('id','title')
	list_editable = ('is_published',)

class ComnentAdmin(admin.ModelAdmin):
	list_display = ('id','name','is_published','time')
	list_display_links = ('id','name')
	list_editable = ('is_published',)

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Comment,ComnentAdmin)