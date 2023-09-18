from django import forms
from .models import *


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ["created_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["topic"].required = False
        self.fields["publish"].required = False
        self.fields["views"].required = False
        self.fields["author_id"].required = False
        self.fields["modified"].required = False
