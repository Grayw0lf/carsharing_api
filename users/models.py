import jwt
from datetime import datetime, timedelta

from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CarShareUserManager


class CarShareUser(AbstractBaseUser):
    username = models.CharField(max_length=255, db_index=True, unique=True)
    email = models.EmailField(validators=[validators.validate_email],
                              unique=True,
                              blank=True)
    user_lang = models.CharField(max_length=10,
                                 choices=settings.LANGUAGES,
                                 default=settings.LANGUAGE_CODE,
                                 verbose_name=_('Язык интерфейса'))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    object = CarShareUserManager()

    def __str__(self):
        return self.email

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
