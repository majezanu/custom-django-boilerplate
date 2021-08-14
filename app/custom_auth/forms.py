from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordResetForm
from django import forms
from django.conf import settings
from .models import CustomUser
from .notification import ResetPasswordNotification

class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
         user = context.get('user')
         user.notify(ResetPasswordNotification(subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name))
    

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email','password1', 'password2')

    def save(self, commit = True):
        user = super(CustomSignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user