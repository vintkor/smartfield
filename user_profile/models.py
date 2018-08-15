from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext as _
from user_profile.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Пользователи системы
    """
    email = models.EmailField(verbose_name=_('email'), max_length=255, unique=True, db_index=True)
    avatar = models.ImageField(verbose_name=_('Аватар'), blank=True, null=True, upload_to="user/avatar")
    first_name = models.CharField(verbose_name=_('Фамилия'), max_length=40)
    last_name = models.CharField(verbose_name=_('Имя'), max_length=40)
    login = models.CharField(max_length=30, verbose_name=_('Логин'), unique=True)
    is_admin = models.BooleanField(_('Суперпользователь'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        if self.first_name and self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        elif self.first_name:
            return '{} {}'.format(self.first_name, self.email)
        elif self.last_name:
            return '{} {}'.format(self.last_name, self.email)
        else:
            return self.email

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def is_staff(self):
        return self.is_admin
