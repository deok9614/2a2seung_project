from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    article_slug = models.SlugField("slug", null=True, blank=False, unique=True)
    content = HTMLField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    # is_draft = models.BooleanField(default=False)
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)

    def __str__(self):
        return self.title

    def slug(self):
        return self.article_slug
