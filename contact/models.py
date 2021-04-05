from django.db import models
from phone_field import PhoneField

# Create your models here.


class Contact(models.Model):
    """ Model to create Contact Form """
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    phone_number = PhoneField(max_length=20, blank=True)
    message = models.TextField(max_length=1500, null=False, blank=False)

    def __str__(self):
        return f'Contact form from {self.name}'
