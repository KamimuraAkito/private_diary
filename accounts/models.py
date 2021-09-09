<<<<<<< HEAD
=======
from django.db import models
>>>>>>> 637cc7e2b20dbc6de5db8ea1220c1b221e785217
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
<<<<<<< HEAD
=======
    #拡張ユーザーモデル
>>>>>>> 637cc7e2b20dbc6de5db8ea1220c1b221e785217

    class Meta:
        verbose_name_plural = 'CustomUser'