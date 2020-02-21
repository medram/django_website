import os
import secrets
from PIL import Image

from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

from account.models import Profile


def _user_profile_path(instance, filename):	
	return f'profiles/{secrets.token_hex(16)}.jpg'

def _post_image_path(instance, filename):
	now = timezone.now()
	return f'photos/{now.year}/{now.month:02d}/{secrets.token_hex(16)}.jpg'


class Category(models.Model):
	class Meta:
		verbose_name_plural = 'Categories'

	name = models.CharField(max_length=32, unique=True)
	slug = models.SlugField()
	parent_cat = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.name


class City(models.Model):
	class Meta:
		verbose_name_plural = 'Cities'
	
	name = models.CharField(max_length=32, unique=True)
	slug = models.SlugField(max_length=32, unique=True)

	def __str__(self):
		return self.name


class Post(models.Model):
	class Status(models.IntegerChoices):
		APPROVED = (1, 'approved')
		REJECTED = (2, 'rejected')
		PENDING  = (3, 'pending')

	title 	= models.CharField(max_length=256)
	desc 	= models.TextField()
	price 	= models.IntegerField(blank=True, default=0)
	status 	= models.IntegerField(choices=Status.choices, default=Status.PENDING)
	is_published = models.BooleanField(default=0, blank=True)
	main_image = models.ImageField(upload_to=_post_image_path)
	image_1 = models.ImageField(upload_to=_post_image_path, blank=True)
	image_2 = models.ImageField(upload_to=_post_image_path, blank=True)
	image_3 = models.ImageField(upload_to=_post_image_path, blank=True)
	image_4 = models.ImageField(upload_to=_post_image_path, blank=True)
	image_5 = models.ImageField(upload_to=_post_image_path, blank=True)
	created = models.DateTimeField(auto_now_add=True, blank=True)
	updated = models.DateTimeField(auto_now=True, blank=True)

	# Foreign keys
	profile 	= models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	category 	= models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
	city 		= models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)

	def get_images(self):
		images = [self.main_image]
		if self.image_1:
			images.append(self.image_1)

		if self.image_2:
			images.append(self.image_2)

		if self.image_3:
			images.append(self.image_3)

		if self.image_4:
			images.append(self.image_4)

		if self.image_5:
			images.append(self.image_5)

		if self.image_5:
			images.append(self.image_5)
		return images

	def save(self, *args, **kwargs):
		# delete the old images.
		try:
			post = Post.objects.filter(pk=self.pk).first()
			new_list = self.get_images()
			old_list = post.get_images()
			
			for im, old_im in zip(new_list, old_list):
				if im.name != old_im.name:
					print('>', old_im.path)
					os.remove(old_im.path)

		except IOError:
			pass

		# save the Post
		super().save(*args, **kwargs)

		# resizing post images.
		size = (900, 900)
		for image in self.get_images():
			try:
				if image.width > size[0] or image.height > size[1]:
					#print('resizing', image.path)
					im = Image.open(image.path)
					im.thumbnail(size)
					im = im.convert('RGB')
					im.save(image.path, format='JPEG')
			except IOError:
				pass

	def __str__(self):
		return self.title


