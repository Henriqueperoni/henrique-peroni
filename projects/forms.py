from django import forms
from .widgets import CustomClearableFileInput
from .models import Project


class PostForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'live_site',
                  'github', 'thumbnail_image',)

        description_image = forms.ImageField(label='Image',
                                             required=True,
                                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus no first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Post Title',
            'description': 'Description',
            'live_site': 'Live Site URL',
            'github': 'GitHub URL',
            'thumbnail_image': 'Thumbnail Image',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-contact'
            self.fields[field].label = False
