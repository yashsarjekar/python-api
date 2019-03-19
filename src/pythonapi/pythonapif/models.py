from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
#create your model here
class UserProfileManager(BaseUserManager):
    """Helps Django to use our custom user model."""
    def CreateUser(self, email, name, password = None):
        """Creates a new user profile object."""
        if not email:
            raise ValueError('Users Must have Email Address')
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save(using = self._db)
        return user


    def CreateSupperUser(self, email, name, password):
        """Create the user a Supper User."""
        user = self.CreateUser(email, name, password)
        user.is_supperuser = True
        user.is_staff = True
        user.save(using = self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents the "user profile" inside our system."""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """Used to get User Full name."""
        return self.name
    
    def get_short_name(self):
        """Used to get User Short Name."""
        return self.name

    def __str__(self):
        """Django uses to convert object into string."""
        return self.email