from django.urls import path, include
<<<<<<< HEAD
from .views import IndexView, page_not_found, server_error
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("500/", server_error, name="server_error"),
    path("404/", page_not_found, name="page_not_found"),
=======

from .views import IndexView
from core.views import pagina_nao_encontrada, erro_servidor

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
<<<<<<< HEAD
>>>>>>> a8c0174 (include core app and configs)
=======
    path("404/", pagina_nao_encontrada, name="pagina_nao_encontrada"),
    path("500/", erro_servidor, name="erro_servidor")
>>>>>>> d3380e7 (add corrections)
]

# paginas e Erro
handler404 = 'core.views.pagina_nao_encontrada'
handler500 = 'core.views.erro_servidor'