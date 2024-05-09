# This file is where we'll list our blog app-specific URLs.

from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
]