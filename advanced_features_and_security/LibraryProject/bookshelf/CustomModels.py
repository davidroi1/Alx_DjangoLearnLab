from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.db import models


class CustomUserModel(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to='/relationship_app/image')

    def __str__(self):
        return f"{self.date_of_birth} {self.profile_photo}"