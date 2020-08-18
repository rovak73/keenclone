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
from specialties.models import Specialty


class Profile(models.Model):
    # CHOICES
    SPECIALTIES_CHOICES = (
        ('01', 'Clarividencia'),
        ('02', 'Exploración de Sueños'),
        ('03', 'Tarot'),
        ('04', 'Numerancia'),
        ('05', 'Péndulo'),
        ('06', 'Carta Kármica'),
    )
    # DATABASE FIELDS

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True
        )
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics', max_length=255, null=True, blank=True)
    profile_name = models.CharField(unique=True, max_length=255, null=True, blank=True)
    slug = AutoSlugField(populate_from='profile_name')
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    country = models.CharField(max_length=32, null=True, blank=True)
    rut = models.CharField(max_length=12, null=True, blank=True)
    profile = models.TextField(max_length=1280, null=True, blank=True)
    profile_excerpt = models.TextField(max_length=280, null=True, blank=True)
    specialty =  models.ManyToManyField('specialties.Specialty', null=True, blank=True)
        
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
        self.slug = slugify(self.profile_name)
        super().save(*args, **kwargs)

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('profile:profile-detail', kwargs={'slug': self.slug})

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()