from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager

from web.enums import Category


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, commit=True, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(unique=True, max_length=320, verbose_name="Почта")
    name = models.CharField(max_length=63, verbose_name="Имя", null=True)
    chat_id = models.IntegerField(null=True)

    USERNAME_FIELD = "email"

    @property
    def is_staff(self):
        return self.is_superuser


class BaseModel(models.Model):
    title = models.CharField(max_length=127, verbose_name="Название")
    category = models.CharField(
        max_length=15,
        choices=Category.choices,
        default=Category.other,
        verbose_name="Категория"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name="Сумма")

    class Meta:
        abstract = True


class Spending(BaseModel):
    created_at = models.DateTimeField(auto_now_add=True)


class Reminder(BaseModel):
    text = models.TextField(null=True, verbose_name="Описание")
    remind_at = models.DateTimeField(verbose_name="Напомнить")
