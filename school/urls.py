from .views import SchoolCreateView, SchoolDeleteView, SchoolDetailView, SchoolUpdateView, SchoolListView
from django.urls import path


urlpatterns = [
    path("", SchoolListView.as_view(), name="school_all"),
    path('<int:pk>/detail', SchoolDetailView.as_view(), name='school_detail'),
    path('new/', SchoolCreateView.as_view(), name='school_create'),
    path('<int:pk>/update/', SchoolUpdateView.as_view(), name='school_update'),
    path('<int:pk>/delete/', SchoolDeleteView.as_view(), name='school_delete'),
]
