from django.db import models
from django.contrib.auth.models import User
import uuid



# Create your models here.

# Skip: Models:
#           Profile: short_intro, bio, profile_image, social_github, social_twitter, social_linkedin,
#           social_youtube, social_website
#           Skill: owner, name, description, created, id
#       Templates:
#           User-profile.html
#       View:
#
#


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)  
    email = models.EmailField(max_length=500, blank=True, null=True)    
    location = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)


