from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser)

# Create your models here.


class AuthUser(AbstractUser):
    # username = models.CharField(max_length=255, unique=True, db_index=True, blank=True)
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

class Transaction(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    amount = models.FloatField()
    address = models.CharField(max_length=100)
    memo = models.CharField(max_length=100)
    sent = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.memo} {self.address}"

class AvailableBtc(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    btc = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

