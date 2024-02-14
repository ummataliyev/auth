"""
telegram user model
"""
from django.contrib.auth.models import AbstractUser

from apps.users.models.base import models
from apps.users.models.base import BaseModel


class TGUser(
    AbstractUser,
    BaseModel
):
    """
    custom user model.
    """
    is_active = models.BooleanField(default=False)
    chat_id = models.BigIntegerField(unique=True, null=False)
    phone_number = models.BigIntegerField(null=True, unique=True)
    code = models.CharField(max_length=6, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'chat_id'

    class Meta:
        """
        meta fields.
        """
        db_table = "users"
