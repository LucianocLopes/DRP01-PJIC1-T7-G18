from django.urls import path, include

from .views import IndexView
from core.views import pagina_nao_encontrada, erro_servidor

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("404/", pagina_nao_encontrada, name="pagina_nao_encontrada"),
    path("500/", erro_servidor, name="erro_servidor")
]

# paginas e Erro
handler404 = 'core.views.pagina_nao_encontrada'
handler500 = 'core.views.erro_servidor'