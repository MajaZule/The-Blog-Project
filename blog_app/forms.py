from django import forms
from blog_app.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        fields = ('author', 'text')
        widgets = {
            'author':forms.TextInput(),
            'text':forms.Textarea()
        }
