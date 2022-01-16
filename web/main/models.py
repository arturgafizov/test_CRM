from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractUser):

    class StatusChoice(models.TextChoices):
        CLIENT = ('client', 'Client')
        EMPLOYEE = ('employee', 'Employee')

    username = None
    email = models.EmailField(_('Email address'), unique=True)
    status = models.CharField(max_length=8, choices=StatusChoice.choices)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    phone = PhoneNumberField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    def full_name(self):
        return super().get_full_name()
