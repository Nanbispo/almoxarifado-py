from rest_framework.decorators import api_view
from rest_framework.response import Response

from controllers.department_controller import DepartmentController
from database import get_connection
from services.department_service import DepartmentService
from use_cases.department_use_cases import DepartmentUseCases


def _build_department_controller(connection):
    service = DepartmentService(connection)
    use_cases = DepartmentUseCases(service)
    return DepartmentController(use_cases)


@api_view(["GET", "POST"])
def departments(request):
    connection = get_connection()
    try:
        controller = _build_department_controller(connection)
        if request.method == "GET":
            body, response_status = controller.list_departments()
        else:
            body, response_status = controller.create_department(request.data)
        return Response(body, status=response_status)
    finally:
        connection.close()


@api_view(["GET", "PUT"])
def department_detail(request, department_id):
    connection = get_connection()
    try:
        controller = _build_department_controller(connection)
        if request.method == "GET":
            body, response_status = controller.get_department(department_id)
        else:
            body, response_status = controller.update_department(
                department_id, request.data
            )
        return Response(body, status=response_status)
    finally:
        connection.close()
