from django.urls import path
from django.conf.urls import url
from . import views

app_name = "custom_auth"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("reset-password/", views.PasswordResetView.as_view(), name="reset_password"),
    path("reset-password-done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    url(r'^reset-password-done-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("signup/", views.SignupView.as_view(), name="register"),
]