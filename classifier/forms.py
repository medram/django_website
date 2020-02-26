from django import forms
from .models import Post, City, Category
from crispy_forms.helper import FormHelper
from . import choices

class AnnouncementCreationFrom(forms.ModelForm):
	#category 	= forms.IntegerField(widget=forms.Select(choices=[(0, '---- Select a category ----')] + [(cat.pk, cat.name) for cat in choices.categories()]))
	#city 		= forms.IntegerField(widget=forms.Select(choices=[(city.pk, city.name) for city in choices.cities()]))
	category 	= forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='---- Select a category ----')
	city 		= forms.ModelChoiceField(queryset=City.objects.all(), empty_label='---- Select a city ----')
	
	class Meta:
		model = Post
		fields = ('category', 'city', 'title', 'desc', 'price', 'main_image',
			'image_1', 'image_2', 'image_3', 'image_4', 'image_5')

		widgets = {
			'main_image': forms.FileInput(),
			'image_1': forms.FileInput(),
			'image_2': forms.FileInput(),
			'image_3': forms.FileInput(),
			'image_4': forms.FileInput(),
			'image_5': forms.FileInput()
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.use_custom_control = True
		self.helper.form_tag = False

	def save(self, *args, **kwargs):
		user = kwargs.pop('user', '')
		obj = super().save(commit=False)
		obj.profile = user.profile
		return obj.save()