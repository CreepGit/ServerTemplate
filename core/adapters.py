from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialLogin
from django.contrib.auth import get_user_model
from django.forms import ValidationError
import random
from django.contrib.auth import get_user_model


class CoreAccountAdapter(DefaultAccountAdapter):
    """Core app customization for account adapter

    https://django-allauth.readthedocs.io/en/latest/advanced.html#creating-and-populating-user-instances
    """

    def save_user(self, request, user, form):
        user = super().save_user(request, user, form, commit=False)
        User = get_user_model()
        for _ in range(10**4):
            slug = str(random.randint(10**6, 10**8))
            print("Slug", slug)
            if User.objects.filter(slug=slug).exists():
                continue  # Look for another slug as this one is already in use
            user.slug = slug
        user.save()


class CoreSocialAccountAdapter(DefaultSocialAccountAdapter):
    pass
