from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from . import views
from mediafiles.views import downloads_view

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("login/email/", views.email_login_view, name="email_login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("profile/", views.profile_view, name="profile"),

    path(
        "password_reset/",
        RedirectView.as_view(
            url=reverse_lazy("accounts:email_login"),
            permanent=False,
        ),
        name="password_reset",
    ),

    path("downloads/", downloads_view, name="downloads"),
]
