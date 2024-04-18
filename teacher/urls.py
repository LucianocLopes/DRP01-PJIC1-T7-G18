<<<<<<< HEAD
from django.urls import path, include

from .views import TeacherGroupView, TeacherListView, TeacherCreateView

urlpatterns = [   
    path("", TeacherListView.as_view(), name="teacher_all"),
    path("new/", TeacherCreateView.as_view(), name="teacher_new"),
    path("<int:pk>/detail/", TeacherGroupView.as_view(), name="teacher_detail"),
=======
from .views import TeacherCreateView, TeacherDeleteView, TeacherDetailView, TeacherUpdateView, TeacherListView
from django.urls import path


urlpatterns = [
    path("", TeacherListView.as_view(), name="teacher_all"),
    path('<int:pk>/detail', TeacherDetailView.as_view(), name='teacher_detail'),
    path('new/', TeacherCreateView.as_view(), name='teacher_create'),
    path('<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),
>>>>>>> ee2e9db (add, configurate and edit app teacher)
]
