from django import forms
from .models import Project


class PostForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'description1'
                  'description2', 'live_site', 'github',
                  'description_image', 'description_image1',
                  'description_image2')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
