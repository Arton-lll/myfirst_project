from django.db import models
from django.utils import timezone
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('タイトル',max_length=200)
    text = models.TextField('本文')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=False, null=True)
    tags = TaggableManager('タグ',blank=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
