from .views import DisciplineCreateView, \
    DisciplineDeleteView, DisciplineDetailView, DisciplineUpdateView, \
    DisciplineListView, GraduationCreateView, \
    GraduationDeleteView, GraduationDetailView, GraduationUpdateView, \
    GraduationListView

from django.urls import path


urlpatterns = [
    path("", DisciplineListView.as_view(), name="discipline_all"),
    path('<int:pk>/detail', DisciplineDetailView.as_view(),
         name='discipline_detail'),
    path('new/', DisciplineCreateView.as_view(), name='discipline_create'),
    path('<int:pk>/update/', DisciplineUpdateView.as_view(),
         name='discipline_update'),
    path('<int:pk>/delete/', DisciplineDeleteView.as_view(),
         name='discipline_delete'),

    path("graduation/", GraduationListView.as_view(), name="graduation_all"),
    path('graduation/<int:pk>/detail', GraduationDetailView.as_view(),
         name='graduation_detail'),
    path('graduation/new/', GraduationCreateView.as_view(),
         name='graduation_create'),
    path('graduation/<int:pk>/update/', GraduationUpdateView.as_view(),
         name='graduation_update'),
    path('graduation/<int:pk>/delete/', GraduationDeleteView.as_view(),
         name='graduation_delete'),
]
