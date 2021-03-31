import random
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from PIL import Image


""" Custom user model here. """
# UserModel starts here.
def image_upload_destination(instance, filename):
    if filename:
        get_extension = filename.split('.')[-1]
        get_filename = random.randint(0, 1000000000000)
        new_filename = f"IMG{get_filename}UN{instance.user.username}.{get_extension}"
        return(f'djangoadmin/{instance.user.id}_{instance.user.username}/{new_filename}')

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to=image_upload_destination)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        ordering = ['pk']
        verbose_name = 'User'
        verbose_name_plural = 'Users'  

# usermodel method here.
def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        UserModel.objects.create(user=kwargs['instance'])
post_save.connect(create_user_profile, sender=User)