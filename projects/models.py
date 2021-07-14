from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.


class Project(models.Model):

    class Meta:
        verbose_name_plural = 'Projects'

    name = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    slug = models.CharField(max_length=256, blank=True, unique=True)
    description = RichTextField(
        max_length=5000, null=False, blank=False)
    live_site = models.URLField(max_length=200, null=False, blank=False)
    github = models.URLField(max_length=200, null=False, blank=False)
    thumbnail_image = models.ImageField(null=False, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Create slug for SEO
        # Don't ever change once established since is part of the URI
        if self.slug is None or self.slug == '':
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
