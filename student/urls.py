from .views import StudentCreateView, StudentDeleteView, StudentDetailView, StudentUpdateView, StudentListView
from django.urls import path


urlpatterns = [
    path("", StudentListView.as_view(), name="student_all"),
    path('<int:pk>/detail', StudentDetailView.as_view(), name='student_detail'),
    path('new/', StudentCreateView.as_view(), name='student_create'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
