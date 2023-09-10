from django.db import models
import uuid

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db import models

from core.abstract.models import AbstractModel, AbstractManager

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.public_id, filename)

class UserManager(BaseUserManager, AbstractManager):
    def get_object_by_public_id(self, public_id):
        try:
           instance = self.get(public_id=public_id)
           return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
        
    def create_user(self, username, email, password=None,**kwargs):
        """Create and return a `User` with an email, phone number,username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address.')
        if password is None:
            raise TypeError('Users must have a password.')
        
        user = self.model(username=username, email=self.normalize_email(email),**kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, password=None,**kwargs):
        """Create and return a `User` with superuser (admin) permissions."""
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email address.')
        if username is None:
            raise TypeError('Superusers must have a username.')

        user = self.create_user(username, email, password,**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractModel,AbstractBaseUser,PermissionsMixin):
    username = models.CharField(db_index=True,max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    bio = models.TextField(blank=True)
    avator = models.ImageField(null=True, blank=True, upload_to=user_directory_path)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"