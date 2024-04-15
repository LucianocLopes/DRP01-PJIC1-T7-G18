from django.urls import path, include
<<<<<<< HEAD
from .views import IndexView, page_not_found, server_error
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("500/", server_error, name="server_error"),
    path("404/", page_not_found, name="page_not_found"),
=======

from .views import IndexView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
>>>>>>> a8c0174 (include core app and configs)
]
