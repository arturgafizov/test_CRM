from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Lead(models.Model):

    class LeadsStatus(models.TextChoices):
        PROCESSING = ('processing', 'Processing')
        INACTIVE = ('inactive', 'Inactive')

    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leads')
    status = models.CharField(max_length=10, choices=LeadsStatus.choices, default=LeadsStatus.INACTIVE)
    objects = models.Manager()
