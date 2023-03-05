from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
    
    #def has_perm(self, perm, obj=None):
    #    return self.is_superuser

    #def has_module_perms(self, users):
    #    return self.is_superuser

    @property
    def is_admin(self):
        return self.is_staff and self.is_superuser

    @property
    def is_teacher(self):
        return self.groups.filter(name='teacher').exists()

    @property
    def is_parent(self):
        return self.groups.filter(name='parent').exists()