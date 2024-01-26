"""
base models
"""
from django.db import models


class BaseModel(models.Model):
    """
    abstract base model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        the base model meta class fields.
        """
        abstract = True
