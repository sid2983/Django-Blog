from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    #we can do auto_now=True or auto_now_add=True
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        return reverse('djblog:djblog-post-detail',kwargs={'pk':self.pk})