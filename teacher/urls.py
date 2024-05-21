from django.urls import path, include

from .views import TeacherGroupView, TeacherListView, TeacherCreateView

urlpatterns = [   
    path("", TeacherListView.as_view(), name="teacher_all"),
    path("new/", TeacherCreateView.as_view(), name="teacher_new"),
    path("<int:pk>/detail/", TeacherGroupView.as_view(), name="teacher_detail"),
]
