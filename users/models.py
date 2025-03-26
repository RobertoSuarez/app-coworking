from django.db import models
from django.contrib.auth.models import User
import pyotp


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    location = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    otp_secret = models.CharField(
        max_length=64, default=pyotp.random_base32, blank=True
    )

    def __str__(self):
        return self.user.username

    def generate_otp(self):
        totp = pyotp.TOTP(self.otp_secret)
        return totp.now()

    def verify_otp(self, otp):
        totp = pyotp.TOTP(self.otp_secret)
        return totp.verify(otp)
