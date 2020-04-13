from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve shot name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email





# class UserProfileManager(BaseUserManager):
#     """Manager for user profiles"""

#     def create_user(self, email, name, password=None):
#         """Create a new user profile"""
#         if not email: 
#             raise ValueError('User must have an email address')
        
#         # letter case second half of email address
#             email = self.normalize_email(email)
#         # creates a user model 
#         # and sets the email and the name 
#             user = self.model(email=email, name=name)

#         # part of the AbstractBaseUser
#         # Reason for this is to converted to a hash 
#         # hacker would only be able to see the hashed password
#             user.set_password(password)
#             user.save(using=self._db)

#         # return newly create user object
#         return user

#         def create_superuser(self, email, name, password):
#             """Create and save a new superuser wuth given details"""
#             user = self.create_user(email, name, password )

#             # create by the PermissionsMixin
#             user.is_superuser = True
#             user.is_staff = True 
#             user.save(using=self._db)

#             return user

# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     """Database model for users in the system"""
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True) # if a user's profile is active
#     is_staff = models.BooleanField(default=False) # if user is staff = Admin

#     objects = UserProfileManager() #going to create class later

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         """Retrieve full name of user"""
#         return self.name

#     def get_short_name(self):
#         """Retieve short name of user"""
#         return self.name

#     def __str__(self):
#         """Return string representation of our user"""
#         return self.email