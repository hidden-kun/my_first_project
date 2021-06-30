from rest_framework import views
from course.models import Student , Group , Branch
from django.urls import path
from course.views import BranchAPIView, StudentCreateView, StudentDetailView, StudentListView, BranchCreateView, BranchDetailView, BranchListView, BranchUpdateView, GroupCreateView, GroupDetailView, GroupListView, GroupUpdateView, StudentUpdateView, branch_edit, group_edit, my_groups, my_main_page, my_students, student_create, student_detail , group_detail, group_create, student_edit, branch_create


urlpatterns = [
    path('', my_main_page, name='my_main_page'),
    path('branches/', BranchListView.as_view(), name='branches-list'),
    path('branch/<int:branch_id>/', BranchDetailView.as_view(), name='branch_detail'),
    path('branch/create/', BranchCreateView.as_view(), name='branch_create'),
    path('branches/<int:branch_id>/edit/',BranchUpdateView.as_view(), name='branch_edit'),

    path('students/', StudentListView.as_view(), name='students'),
    path('students/<int:student_id>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:student_id>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),


    path('groups/', GroupListView.as_view(), name='groups'),
    path('groups/<int:group_id>/', GroupDetailView.as_view(), name='group_detail'),
    path('groups/<int:group_id>/edit', GroupUpdateView.as_view(), name='group_edit'),
    path('groups/create/', GroupCreateView.as_view(), name='group_create'),

    path('api/branches', BranchAPIView.as_view(),name='api_branches')
]