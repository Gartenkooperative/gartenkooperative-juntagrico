"""juntagrico stats URL Configuration
"""
from django.urls import path

from . import views

app_name = 'jst'
urlpatterns = [
    # assignments
    path('assignments/export', views.assignments_export, name='export-assignments'),
    path('assignments', views.assignments, name='view-assignments'),
    path('assignments/<slug:trunc>', views.assignments, name='view-assignments-by'),
]
