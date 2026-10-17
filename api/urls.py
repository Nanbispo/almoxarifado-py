from django.urls import path

from api.views import department_detail, departments

urlpatterns = [
    path("departments/", departments, name="departments"),
    path("departments/<int:department_id>/", department_detail, name="department-detail"),
]
