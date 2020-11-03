from django.contrib import admin

# Register your models here.
from companions.models import UserProfileModel, User

admin.site.register(UserProfileModel) 
