from allauth.account.forms import SignupForm
from django import forms
from core.models import User


class CoreSignupForm(SignupForm):
    username_field = forms.CharField(
        max_length=20,
        min_length=4,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Username", "autofocus": True}),
    )

    def save(self, request):
        user: User = super(CoreSignupForm, self).save(request)  # type: ignore
        user.username = self.cleaned_data["username_field"]
        user.save()
        return user
