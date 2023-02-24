from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import string


def specifier_validator(value: str):
    alloweds = set(string.ascii_uppercase + string.digits)
    if len(value) != 4:
        raise ValidationError(
            f"Specifier must be exactly 4 characters (not {len(value)})",
            params={"value": value},
        )
    for c in set(value):
        if c not in alloweds:
            raise ValidationError(
                "Specifier can only contain uppercase letters and digits",
                params={"value": value},
            )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        "username",
        max_length=30,
        unique=False,
        help_text="Required. 30 unicode characters or fewer.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    specifier = models.CharField(
        "specifier",
        max_length=4,
        unique=False,
        blank=False,
        help_text="Required. 4 characters. Uppercase letters and digits only.",
        validators=[specifier_validator],
    )
    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={
            "unique": "A user with that email address already exists.",
        },
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
    REQUIRED_FIELDS = ["specifier", "username"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        constraints = [models.UniqueConstraint(
            fields=["username", "specifier"], name="Unique username + specifier"
        )]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        self.username = self.username.lower()
        self.specifier = self.specifier.upper()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_name_with_specifier(self):
        return f"{self.username}#{self.specifier}"
