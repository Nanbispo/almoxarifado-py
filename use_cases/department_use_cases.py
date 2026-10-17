from services.department_service import DepartmentService


class DepartmentNotFoundError(Exception):
    """Raised when a requested department does not exist."""


class InvalidDepartmentNameError(Exception):
    """Raised when a department name is missing or blank."""


class DepartmentUseCases:
    def __init__(self, department_service: DepartmentService):
        self.department_service = department_service

    def list_departments(self):
        return self.department_service.get_all_Department()

    def get_department(self, department_id: int):
        department = self.department_service.get_by_id_Department(department_id)
        if department is None:
            raise DepartmentNotFoundError
        return department

    def create_department(self, name: str):
        clean_name = self._validate_name(name)
        self.department_service.insert_Department(clean_name)

    def update_department(self, department_id: int, name: str):
        clean_name = self._validate_name(name)
        self.get_department(department_id)
        self.department_service.update_Department(department_id, clean_name)
        return {"id": department_id, "name": clean_name}

    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            raise InvalidDepartmentNameError
        return name.strip()
