from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True) 

    def __str__(self):
        return self.phone_number