from django.contrib import admin
from .models import Menu, MenuItem, Page


class PageAdmin(admin.ModelAdmin):
	list_per_page = 25
	list_display = ('title', 'slug', 'published', 'created', 'updated')
	list_editable = ('published',)
	list_filter = ('published',)
	search_fields = ('title', 'slug')


class InLineMenuItem(admin.TabularInline):
	model = MenuItem
	extra = 0
	# max_num = 7


class MenuAdmin(admin.ModelAdmin):
	inlines = (InLineMenuItem,)
	list_display = ('name', 'total_menu_items')

	def total_menu_items(self, obj):
		return MenuItem.objects.filter(menu=obj.pk).count()

	def has_delete_permission(self, request, obj=None):
		return False

	def has_add_permission(self, request, obj=None):
		return False

# admin.site.site_header = 'site header'
# admin.site.site_title = 'site title'
# admin.site.index_title = 'index title'

admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
