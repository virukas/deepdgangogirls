from pyexpat import model
from django.db import models

from django.conf import settings

from django.utils import timezone

# Create your models here.


class Post (models.Model):
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.question
    def __str__(self):
        return self.choice_text

    def __str__(self):
        return self.title+str(self.id)

    