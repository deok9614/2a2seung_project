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

    # title = forms.CharField(max_length=200)
    # content = forms.CharField(widget=forms.Textarea)
    # image = forms.ImageField(required=False)  # 이미지는 선택 사항
    # is_draft = forms.BooleanField(required=False, initial=True)  # 체크 박스 기본값은 '임시 저장'으로 설정
