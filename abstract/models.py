from django.db import models


class AbstractModel(models.Model):
    """
    This will be use as an abstract model for all other models
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
