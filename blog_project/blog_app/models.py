from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255, default="전체")
    publish = models.CharField(max_length=1, default="Y")
    views = models.IntegerField(default=0)
    author_id = models.AutoField(primary_key=True)
    # subtitle = models.CharField(max_length=200, default="", blank=True)
    # article_slug = models.SlugField("slug", null=True, blank=False, unique=True)
    # image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    # is_draft = models.BooleanField(default=False)
    # published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # '..' 문자열이 포함된 content 필드를 변경
        self.content = self.content.replace('"..', '"')
        super().save(*args, **kwargs)

    # def slug(self):
    #     return self.article_slug
