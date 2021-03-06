from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserChangeForm(auth_forms.UserChangeForm):
    password = None

    class Meta(auth_forms.UserChangeForm.Meta):
        model = User
        fields = ("name", "email",)


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = ("username", "name", "email",)
