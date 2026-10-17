from rest_framework import status

from use_cases.department_use_cases import (
    DepartmentNotFoundError,
    DepartmentUseCases,
    InvalidDepartmentNameError,
)


class DepartmentController:
    def __init__(self, department_use_cases: DepartmentUseCases):
        self.department_use_cases = department_use_cases

    def list_departments(self):
        departments = self.department_use_cases.list_departments()
        body = [{"id": department.id, "name": department.name} for department in departments]
        return body, status.HTTP_200_OK

    def get_department(self, department_id: int):
        try:
            department = self.department_use_cases.get_department(department_id)
            return {"id": department.id, "name": department.name}, status.HTTP_200_OK
        except DepartmentNotFoundError:
            return {"detail": "Departamento não encontrado."}, status.HTTP_404_NOT_FOUND

    def create_department(self, payload):
        try:
            self.department_use_cases.create_department(self._name_from_payload(payload))
            return {"message": "Departamento criado com sucesso."}, status.HTTP_201_CREATED
        except InvalidDepartmentNameError:
            return self._invalid_name_response()

    def update_department(self, department_id: int, payload):
        try:
            department = self.department_use_cases.update_department(
                department_id, self._name_from_payload(payload)
            )
            return department, status.HTTP_200_OK
        except InvalidDepartmentNameError:
            return self._invalid_name_response()
        except DepartmentNotFoundError:
            return {"detail": "Departamento não encontrado."}, status.HTTP_404_NOT_FOUND

    @staticmethod
    def _invalid_name_response():
        return (
            {"detail": "O campo 'name' é obrigatório e deve ser um texto não vazio."},
            status.HTTP_400_BAD_REQUEST,
        )

    @staticmethod
    def _name_from_payload(payload):
        return payload.get("name") if isinstance(payload, dict) else None
