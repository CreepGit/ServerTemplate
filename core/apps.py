from django.apps import AppConfig
from allauth.account.signals import user_signed_up
import random
import string


def add_missing_user_data(request, user, **kwargs):
    characters = string.ascii_uppercase + string.digits
    if not user.specifier:
        user.specifier = "".join(random.choices(characters, k=4))
        user.save()


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self) -> None:
        user_signed_up.connect(add_missing_user_data)
        return super().ready()
