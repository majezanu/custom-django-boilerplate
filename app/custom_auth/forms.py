from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordResetForm
from django import forms
from django.conf import settings
from django.contrib.auth.models import User

class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)


class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

    def save(self, commit = True):
        user = super(CustomSignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user