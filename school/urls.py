from django.urls import path, include

from .views import *


urlpatterns = [
    path("group/", IndexView.as_view(), name="school_index"),
    path("", SchoolListView.as_view(), name="school_all"),
    path('<int:pk>/update/', SchoolUpdateView.as_view(), name='school_update'),
    path("<int:pk>/detail/", SchoolDetailView.as_view(), name="school_detail"),
    path("<int:pk>/phones/", PhoneSchoolListView.as_view(), name="phones_school_all"),
    path("<int:pk>/address/", AddressSchoolListView.as_view(), name="address_school_all"),
]
