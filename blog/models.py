from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

status = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    title_tag = models.CharField(max_length=256, null=False, blank=False)
    slug = models.CharField(max_length=256, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=status, default=0)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Create slug for SEO
        # Don't ever change once established since is part of the URI
        if self.slug is None or self.slug == '':
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
