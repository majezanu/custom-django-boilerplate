from django.views.generic.edit import CreateView
from django.contrib.auth import views
from django.urls import reverse_lazy
from . import forms

class LoginView(views.LoginView):
  template_name = 'accounts/login.html'
  authentication_form = forms.CustomUserLoginForm
  redirect_authenticated_user = True

class PasswordResetView(views.PasswordResetView):
  template_name = 'accounts/password_reset_form.html'
  html_email_template_name = email_template_name = 'accounts/emails/password_reset_email.html'
  form_class = forms.CustomPasswordResetForm
  success_url = reverse_lazy('custom_auth:password_reset_done')

class PasswordResetDoneView(views.PasswordResetDoneView):
  template_name = 'accounts/password_reset_done.html'

class PasswordResetConfirmView(views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  success_url = reverse_lazy('custom_auth:login')

class SignupView(CreateView):
  template_name = 'accounts/registration.html'
  form_class  = forms.CustomSignupForm
  success_url = reverse_lazy('home')

class LogoutView(views.LogoutView):
  next_page = reverse_lazy('home')
