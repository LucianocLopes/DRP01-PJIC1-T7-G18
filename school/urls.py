from .views import SchoolCreateView, SchoolDeleteView, SchoolDetailView, SchoolUpdateView, SchoolListView, StructListView, StructCreateView, StructDeleteView, StructDetailView, StructUpdateView
from django.urls import path


urlpatterns = [
    path("", SchoolListView.as_view(), name="school_all"),
    path('<int:pk>/detail/', SchoolDetailView.as_view(), name='school_detail'),
    path('new/', SchoolCreateView.as_view(), name='school_create'),
    path('<int:pk>/update/', SchoolUpdateView.as_view(), name='school_update'),
    path('<int:pk>/delete/', SchoolDeleteView.as_view(), name='school_delete'),
    path("struct/", StructListView.as_view(), name="struct_all"),
    path('struct/<int:pk>/detail/',
         StructDetailView.as_view(), name='struct_detail'),
    path('struct/new/', StructCreateView.as_view(), name='struct_create'),
    path('struct/<int:pk>/update/',
         StructUpdateView.as_view(), name='struct_update'),
    path('struct/<int:pk>/delete/',
         StructDeleteView.as_view(), name='struct_delete'),
]
