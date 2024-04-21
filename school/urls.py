<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import path, include

from .views import *


urlpatterns = [
    path("group/", IndexView.as_view(), name="school_index"),
    path("", SchoolListView.as_view(), name="school_all"),
    path('<int:pk>/update/', SchoolUpdateView.as_view(), name='school_update'),
    path("<int:pk>/detail/", SchoolDetailView.as_view(), name="school_detail"),
    path("<int:pk>/phones/", PhoneSchoolListView.as_view(), name="phones_school_all"),
    path("<int:pk>/address/", AddressSchoolListView.as_view(), name="address_school_all"),
=======
from .views import SchoolCreateView, SchoolDeleteView, SchoolDetailView, SchoolUpdateView, SchoolListView
=======
from .views import SchoolCreateView, SchoolDeleteView, SchoolDetailView, SchoolUpdateView, SchoolListView, StructListView, StructCreateView, StructDeleteView, StructDetailView, StructUpdateView
>>>>>>> 98c1c6d (corrects on apps)
from django.urls import path


urlpatterns = [
    path("", SchoolListView.as_view(), name="school_all"),
    path('<int:pk>/detail/', SchoolDetailView.as_view(), name='school_detail'),
    path('new/', SchoolCreateView.as_view(), name='school_create'),
    path('<int:pk>/update/', SchoolUpdateView.as_view(), name='school_update'),
    path('<int:pk>/delete/', SchoolDeleteView.as_view(), name='school_delete'),
<<<<<<< HEAD
>>>>>>> 70b58ba (add app school and config pages)
=======
    path("struct/", StructListView.as_view(), name="struct_all"),
    path('struct/<int:pk>/detail/',
         StructDetailView.as_view(), name='struct_detail'),
    path('struct/new/', StructCreateView.as_view(), name='struct_create'),
    path('struct/<int:pk>/update/',
         StructUpdateView.as_view(), name='struct_update'),
    path('struct/<int:pk>/delete/',
         StructDeleteView.as_view(), name='struct_delete'),
>>>>>>> 98c1c6d (corrects on apps)
]
