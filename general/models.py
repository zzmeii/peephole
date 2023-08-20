from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(to=User, verbose_name='Пользователь', related_name='profile', on_delete=models.DO_NOTHING)
    father_name = models.CharField(verbose_name='Отчество', max_length=64, default='')