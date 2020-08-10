from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from uuslug import uuslug, slugify
from django.db.models.signals import post_save
from autoslug import AutoSlugField


class Profile(models.Model):
    # CHOICES
    SPECIALTIES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    # DATABASE FIELDS

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics', max_length=255, null=True, blank=True)
    profile_name = models.CharField(unique=True, max_length=255, null=True, blank=True)
    slug = models.SlugField(
        unique=False,
        null=False,
        blank=True
        )
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    country = models.CharField(max_length=32, null=True, blank=True)
    rut = models.CharField(max_length=12, null=True, blank=True)
    profile = models.TextField(max_length=1280, null=True, blank=True)
    specialty =  models.CharField(max_length=1, choices=SPECIALTIES, null=True, blank=True)
        
    # MANAGERS
    # objects = models.Manager()
    # user_profiles = UserProfilesManager()

    # META CLASS
    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    # TO STRING METHOD
    def __str__(self):
        return str(self.profile_name)

    # SAVE METHOD
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.profile_name)
        return super().save(*args, **kwargs)
    # def save(self, *args, **kwargs):
    #     self.slug = uuslug(self.profile_name, instance=self)
    #     super(Profile, self).save(*args, **kwargs)
    # def save(self, *args, **kwargs):
    #     self.slug = self.slug or slugify(self.profile_name)
    #     super().save(*args, **kwargs)

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'slug': self.slug})

