from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import random


def user_slug_validator(value: str):
    if len(value) < 4:
        raise ValidationError("Mininum length for slug is 4 characters")


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        "username",
        max_length=64,
        unique=False,
        help_text="Only used as a display name, changeable. Required. 60 unicode characters or fewer.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={
            "unique": "A user with that email address already exists.",
        },
    )
    slug = models.SlugField(
        "url slug",
        max_length=32,
        unique=True,
        blank=False,
        help_text="User's own short unique label for urls, changeable.",
        validators=[user_slug_validator],
    )
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        self.username = self.username.lower()
        if len(self.slug) < 4:
            self.slug = str(random.randint(10**6, 10**8))

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
