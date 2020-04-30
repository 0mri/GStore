from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os


def path_and_rename(prefix, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join(prefix, filename)


def get_path_for_my_model_file(instance, filename):
    return path_and_rename('profile_image/', filename)


class User(AbstractUser):
    profile_image = models.ImageField(
        default='profile_image/default.jpg', upload_to=get_path_for_my_model_file)
