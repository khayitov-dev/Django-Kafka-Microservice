from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .manager import UserManager
from .base import BaseModel



class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """ This Is All User Register Model """

    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
