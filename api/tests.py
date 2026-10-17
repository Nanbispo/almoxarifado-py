from unittest.mock import patch

from rest_framework.test import APITestCase

from models.department import Department


class DepartmentEndpointTests(APITestCase):
    @patch("api.views.DepartmentService")
    @patch("api.views.get_connection")
    def test_lists_departments_and_closes_connection(
        self, get_connection, department_service_class
    ):
        connection = get_connection.return_value
        department_service_class.return_value.get_all_Department.return_value = [
            Department(id=1, name="TI"),
            Department(id=2, name="Compras"),
        ]

        response = self.client.get("/api/departments/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [
                {"id": 1, "name": "TI"},
                {"id": 2, "name": "Compras"},
            ],
        )
        connection.close.assert_called_once_with()
