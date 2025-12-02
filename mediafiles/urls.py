from django.urls import path
from . import views

app_name = "mediafiles"

urlpatterns = [
    path("", views.gallery_view, name="mediafiles"),
]
