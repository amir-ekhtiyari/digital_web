from django.urls import path
from . import views
from mediafiles.views import downloads_view  # ← ویو دانلودها از اپ mediafiles

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("login/email/", views.email_login_view, name="email_login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("profile/", views.profile_view, name="profile"),

    # اضافه کردن مسیر دانلودها
    path("downloads/", downloads_view, name="downloads"),
]
