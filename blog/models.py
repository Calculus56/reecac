from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
# Do research on the Django field types


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        # User,
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    img = models.CharField(max_length=40)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])



