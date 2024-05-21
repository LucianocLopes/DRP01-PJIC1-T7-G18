from django.urls import path, include

from .views import *

urlpatterns = [   
    path("", GroupListView.as_view(), name="group_all"),
    path('<int:pk>/detail', GroupDetailView.as_view(), name='group_detail'),
    path('new/', GroupCreateView.as_view(), name='group_create'),
    path('<int:pk>/update/', GroupUpdateView.as_view(), name='group_update'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
    path("<int:pk>/students-list/",
        GroupStudentsView.as_view(), name="group_students"),
    path("grid", GridGroupListView.as_view(), name="gridgroup_all"),
    path("grid/new/", GridGroupCreateView.as_view(), name="gridgroup_new"),
    path("grid/<int:pk>/detail/", GridGroupDetailView.as_view(), name="gridgroup_detail"),
]
