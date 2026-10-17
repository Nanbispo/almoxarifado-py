from django.urls import path, re_path

from api.views import department_detail, departments

urlpatterns = [
    path("departments/", departments, name="departments"),
    re_path(
        r"^departments/(?P<department_id>[0-9]+)/?$",
        department_detail,
        name="department-detail",
    ),
]
