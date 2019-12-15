from django.contrib import admin
from .models import Product, Category 
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display  = ('id','title','bestseller','featured','price','old_price')
	list_display_links = ('id','title',)
	search_fields = ('title','price')
	list_editable = ('featured','bestseller',)


class CategoryAdmin(admin.ModelAdmin):
	list_display  = ('id','title',)
	list_display_links = ('id','title',)
	search_fields = ('title',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)