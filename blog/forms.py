from django import forms
from .models import PostComment


class CreatePostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('comment', )

    comment = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'comments-form-field',
            'placeholder': 'Leave a comment',
        })
    )
