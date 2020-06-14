from django.db import models
from django.contrib.auth.models import AbstractUser


class ProjectUser(AbstractUser):
    """ Concrete implementation of a project user """
    pass