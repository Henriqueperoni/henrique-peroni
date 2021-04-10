from django import forms
from .models import PostComment


class CreatePostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('comment', )

        comment = forms.CharField(
            label=False,
            widget=forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Leave a comment'
            })
        )
