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
from django.urls import path


urlpatterns = [
    path("", SchoolListView.as_view(), name="school_all"),
    path('<int:pk>/detail', SchoolDetailView.as_view(), name='school_detail'),
    path('new/', SchoolCreateView.as_view(), name='school_create'),
    path('<int:pk>/update/', SchoolUpdateView.as_view(), name='school_update'),
    path('<int:pk>/delete/', SchoolDeleteView.as_view(), name='school_delete'),
>>>>>>> 70b58ba (add app school and config pages)
]
