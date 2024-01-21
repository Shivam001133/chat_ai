from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    email = models.CharField(max_length=225, unique=True)
    phone_number = models.IntegerField(
        unique=True, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    prompt_responce = models.PositiveIntegerField(
        default=0, help_text="No of responce by ai"
    )
    user_suspended = models.BooleanField(default=False)
    delete_history = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class UserProfile(models.Model):

    class ProfileType(models.TextChoices):
        FREE = "F", _("Free")
        PREMIUM = "P", _("Premium")

    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='profile')
    bio = models.TextField(blank=True)
    profile_type = models.CharField(
        max_length=10, choices=ProfileType.choices,
        default=ProfileType.FREE)
    profile_picture = models.ImageField(
        upload_to='./statics/upload_img/user_img/', null=True,
        blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
