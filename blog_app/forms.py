from django import forms
from blog_app.models import Comment
from django.urls import reverse


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author':forms.TextInput(),
            'text':forms.Textarea()
        }
