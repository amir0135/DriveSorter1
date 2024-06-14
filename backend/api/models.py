from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, blank=True)
    tags = models.JSONField(default=list, blank=True)  # New field for tags

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_sorting_method = models.CharField(max_length=255, default='default')

    def __str__(self):
        return self.user.username
