from .views import *
from django.urls import path


urlpatterns = [
    path("", GroupListView.as_view(), name="group_all"),
    path('<int:pk>/detail', GroupDetailView.as_view(), name='group_detail'),
    path('new/', GroupCreateView.as_view(), name='group_create'),
    path('<int:pk>/update/', GroupUpdateView.as_view(), name='group_update'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
    path("<int:pk>/students-list/",
         GroupStudentsView.as_view(), name="group_students"),
]
