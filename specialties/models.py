from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from uuslug import uuslug, slugify
from autoslug import AutoSlugField
from django.conf import settings

# Create your models here.
class Specialty(models.Model):


    specialty_name = models.CharField(unique=True, max_length=128, null=True, blank=True)
    slug = AutoSlugField(populate_from='specialty_name')
    specialty_excerpt = models.CharField(max_length=280, null=True, blank=True)
    specialty_text = models.TextField(max_length=1255, null=True, blank=True)
    picture = models.ImageField(upload_to='specialties_pics', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'specialty'
        verbose_name_plural = 'specialties'

    def __str__(self):
        return str(self.specialty_name)

    def save(self, *args, **kwargs): # new
        self.slug = slugify(self.specialty_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('specialty:specialty-detail', kwargs={'slug': self.slug})
