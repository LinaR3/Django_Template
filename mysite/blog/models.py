from django.db import models
from django.utils import timezone

class Post(models.Model):
    class Status(models.TectChoices):
        DRAF = 'DF', 'Draf'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.ateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                             choices=Status.choices,
                             default=Status.DRAF)
    class Meta: 
        ordering = ['-publish']
        idexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title