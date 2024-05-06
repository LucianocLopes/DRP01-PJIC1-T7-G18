"""
URL configuration for pi1tg18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
=======
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
<<<<<<< HEAD
from django.views.generic import TemplateView

>>>>>>> 86a1e24 (preparing static file folder and template with html test)
=======
from schedule.views import all_events
>>>>>>> a8c0174 (include core app and configs)
=======
from schedule.views import all_events
>>>>>>> 16093fb (created app schedule, config and tests)

urlpatterns = [
    path("", include('core.urls')),
    path('accounts/', include('allauth.urls')),
    path("schedule/", include('schedule.urls')),
    path("school/", include('school.urls')),
    path("teacher/", include('teacher.urls')),
    path("student/", include('student.urls')),
    path("discipline/", include('discipline.urls')),
    path("group/", include('group.urls')),
    path('admin/', admin.site.urls),
    path("all_events/", all_events, name="all_events"),

]
<<<<<<< HEAD
=======

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns


# paginas e Erro
handler404 = 'core.views.pagina_nao_encontrada'
handler500 = 'core.views.erro_servidor'
>>>>>>> d3380e7 (add corrections)
