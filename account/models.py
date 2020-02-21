import os
import secrets
from PIL import Image

from django.db import models
from django.contrib.auth.models import User


def _user_profile_path(instance, filename):
	return f'profiles/{secrets.token_hex(16)}.png'


class Profile(models.Model):
	class Status(models.IntegerChoices):
		PENDING  = (1, 'pending')
		APPROVED = (2, 'approved')
		REJECTED = (3, 'rejected')
		INACTIVE = (4, 'inactive')
		BANNED   = (5, 'banned')

	user 		= models.OneToOneField(User, on_delete=models.CASCADE)
	token		= models.CharField(max_length=64, editable=False)
	profile_image = models.ImageField(upload_to=_user_profile_path, default='profiles/default.jpg', blank=True)
	phone		= models.CharField(max_length=10, blank=True, null=True)
	status 		= models.IntegerField(choices=Status.choices, default=Status.APPROVED)
	created 	= models.DateTimeField(auto_now_add=True, blank=True)
	updated 	= models.DateTimeField(auto_now=True, blank=True)

	def save(self, *args, **kwargs):
		# set the token if not exists.
		if not self.token:
			token = secrets.token_hex(32)
			try:
				while Profile.objects.get(token=token):
					token = secrets.token_hex(32)
			except Profile.DoesNotExist:
				pass
			self.token = token
	
		# getting the old profile images.
		old_profile = None
		try:
			old_profile = Profile.objects.get(user=self.user)
		except Profile.DoesNotExist:
			pass

		# save profile
		super(Profile, self).save(*args, **kwargs)

		# resize profile image.
		size = (200, 200)
		
		try:
			if self.profile_image.name and self.profile_image.name != old_profile.profile_image.name:
				try:
					image = Image.open(self.profile_image.path)
					#image.thumbnail(size)
					image = image.resize(size)
					image.save(self.profile_image.path, 'PNG')
				except IOError:
					pass
				else:
					# removing old profile image.
					try:
						os.remove(old_profile.profile_image.path)
					except IOError:
						pass
		except:
			pass

	def __str__(self):
		return self.user.username
