from django import forms
from .widgets import CustomClearableFileInput
from .models import Project


class PostForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'description1',
                  'description2', 'live_site', 'github',
                  'description_image', 'description_image1',
                  'description_image2')

        description_image = forms.ImageField(
            label='Image', required=True, widget=CustomClearableFileInput)
        description_image1 = forms.ImageField(
            label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus no first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Post Title',
            'description': 'Description',
            'description1': 'Description 1',
            'description2': 'Description 2',
            'live_site': 'Live Site URL',
            'github': 'GitHub URL',
            'description_image': 'Description Image 1',
            'description_image1': 'Description Image 2',
            'description_image2': 'Description Image 3',
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
