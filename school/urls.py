from django.urls import path, include
from core.views import IndexView
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
