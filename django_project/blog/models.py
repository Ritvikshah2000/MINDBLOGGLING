from django.db import models
from django.utils import timezone #for date posted
from django.contrib.auth.models import User #for author, which will be a registered user
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) #foreign key because one author can have multiple posts but a post cannot have multiple authors
    #on_delete deletes posts of author if author is deleted

    def __str__(self): #to print out actualy title of blog when querying from shell
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})
