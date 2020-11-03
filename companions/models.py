from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(blank=True)
    date_of_birth = models.DateField(blank=False)
    def __str__(self):
        return self.user.username