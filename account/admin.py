from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
	# For table columns
	list_display = ('profile', 'user', 'status', 'created', 'updated')
	list_display_links = ('user',)
	list_editable = ('status',)
	list_per_page = 25
	
	# For search
	list_filter = ('status',)
	search_fields = ('phone',)

	def profile(self, obj):
		return format_html(f"<a href=\"{reverse('admin:account_profile_change', args=(obj.pk,))}\"><img src='{obj.profile_image.url}' width='40' height='40' style='border-radius: 50%; border: 1px solid #CCC;'></a>")

# registing models
admin.site.register(Profile, ProfileAdmin)