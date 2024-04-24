<<<<<<< HEAD
from django.urls import path, include

from .views import *

urlpatterns = [   
=======
from .views import *
from django.urls import path


urlpatterns = [
>>>>>>> 93b9589 (add and config new app group)
    path("", GroupListView.as_view(), name="group_all"),
    path('<int:pk>/detail', GroupDetailView.as_view(), name='group_detail'),
    path('new/', GroupCreateView.as_view(), name='group_create'),
    path('<int:pk>/update/', GroupUpdateView.as_view(), name='group_update'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
<<<<<<< HEAD
<<<<<<< HEAD
    path("<int:pk>/students-list/",
        GroupStudentsView.as_view(), name="group_students"),
    path("grid", GridGroupListView.as_view(), name="gridgroup_all"),
    path("grid/new/", GridGroupCreateView.as_view(), name="gridgroup_new"),
    path("grid/<int:pk>/detail/", GridGroupDetailView.as_view(), name="gridgroup_detail"),
=======
>>>>>>> 93b9589 (add and config new app group)
=======
    path("<int:pk>/students-list/",
         GroupStudentsView.as_view(), name="group_students"),
>>>>>>> 64cbb11 (configurations and edits apps)
]
