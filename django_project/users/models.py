from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) #if user is deleted, delete profile
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics') #field for profile picture
    #initially set to default jpeg
    # if uploaded, it is saved in profile_pics dictionary

    def __str__(self): #decides what happens when we print our profile
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)