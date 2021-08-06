from django import forms
from comment.models import Comment2

class CommentForm(forms.ModelForm):
    content = forms.CharField(error_messages={'required': 'Cannot be empty',},
        widget=forms.Textarea(attrs = {'placeholder': 'Please enter the comment' })
    )

    class Meta:
        model = Comment2
        fields = ['content']

