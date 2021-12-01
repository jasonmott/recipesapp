from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import EmailField
from django.utils.translation import gettext_lazy as _

class CustomerManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if other_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_("You must provide an email address"))
        if not username:
            raise ValueError(_("You must provide user name"))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

class Customer(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(blank=True,max_length=100)
    last_name = models.CharField(blank=True,max_length=100)
    email = models.EmailField(
        _("email address"),
        max_length=255,
        unique=True,
    )
    username = models.CharField(blank=False,unique=True,max_length=100)
    profile_image = models.ImageField(blank=True)   
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return "{} {}".format(self.email,self.username)