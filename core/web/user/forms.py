from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from models.user.models import UserModel


class UserModelForm(forms.ModelForm):
    """
    User model form
    """

    template_name = "user/forms/user_form.html"

    class Meta:
        model = UserModel
        fields = [
            "first_name",
            "last_name",
            "full_name",
            "username",
            "email",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"readonly": "readonly"}),
        }


class UserLoginForm(forms.Form):
    """
    User login form
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """
    User registration form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.help_text = ''

    class Meta:
        model = UserModel
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise ValidationError("Passwords do not match")
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 20:
            raise forms.ValidationError("Username must be at most 20 characters long.")
        return username
