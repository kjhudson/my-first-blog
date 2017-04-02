from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now)
    published_date = models.DateTimeField(
        blank = True, null = True)

    #Method publish
    def publish(self):
        self.published_date = timezone.now()
        self.save()
 
    #method __str__ will return the post title as a string when __str__ is called
    def __str__(self):
        return self.title

