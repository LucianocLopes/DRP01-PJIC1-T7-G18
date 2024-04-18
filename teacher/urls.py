from .views import TeacherCreateView, TeacherDeleteView, TeacherDetailView, TeacherUpdateView, TeacherListView
from django.urls import path


urlpatterns = [
    path("", TeacherListView.as_view(), name="teacher_all"),
    path('<int:pk>/detail', TeacherDetailView.as_view(), name='teacher_detail'),
    path('new/', TeacherCreateView.as_view(), name='teacher_create'),
    path('<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),
]
