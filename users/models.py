from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class CarShareUser(AbstractUser):
    user_lang = models.CharField(max_length=10,
                                 choices=settings.LANGUAGES,
                                 default=settings.LANGUAGE_CODE,
                                 verbose_name=_('Язык интерфейса'))

    def __str__(self):
        return self.email
