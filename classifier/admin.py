from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from . import models


class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'price', 'view_publisher', 'is_published', 'status', 'created', 'updated')
	list_display_links = ('id', 'title')
	list_editable = ('status', 'is_published')
	list_per_page = 25

	#fields = ('title', 'price')
	#exclude = ()
	list_filter = ('status', 'is_published')
	search_fields = ('id', 'title', 'price')

	def view_publisher(self, obj):
		return format_html(f"<a href=\"{ reverse('admin:account_profile_change', args=(obj.profile.pk,)) }\" >{obj.profile}</a>")
		

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'parent_cat')
	list_display_links = ('name',)
	list_editable = ('parent_cat',)
	list_per_page = 25

	search_fields = ('id', 'name', 'slug')


class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	list_display_links = ('name',)
	list_per_page = 25

	search_fields = ('name', 'slug')

# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.City, CityAdmin)
