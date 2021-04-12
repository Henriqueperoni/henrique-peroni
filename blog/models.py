from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

status = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    """ Model to save and display posts """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=False, blank=False)
    title_tag = models.CharField(max_length=256, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    slug = models.CharField(max_length=256, unique=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=status, default=0)
    likes = models.ManyToManyField(
        User, related_name='like', default=None, blank=True)
    likes_count = models.BigIntegerField(default='0')
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Create slug for SEO
        # Don't ever change once established since is part of the URI
        if self.slug is None or self.slug == '':
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class PostComment(models.Model):
    """ A model to save and display post comments """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500, null=False, blank=False)
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user}' comment on {self.post}"
