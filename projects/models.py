from django.db import models
from django.utils.text import slugify

# Create your models here.


class Project(models.Model):

    class Meta:
        verbose_name_plural = 'Projects'

    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.CharField(max_length=256, unique=True, blank=True)
    description = models.TextField(max_length=1000, null=False, blank=False)
    description1 = models.TextField(max_length=1000, null=True, blank=True)
    description2 = models.TextField(max_length=1000, null=True, blank=True)
    live_site = models.URLField(max_length=200, null=False, blank=False)
    github = models.URLField(max_length=200, null=False, blank=False)
    description_image = models.ImageField(null=False, blank=False)
    description_image1 = models.ImageField(null=True, blank=True)
    description_image2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Create slug for SEO
        # Don't ever change once established since is part of the URI
        if self.slug is None or self.slug == '':
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
