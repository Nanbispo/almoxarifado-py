from database import get_connection
from services.department_service import DepartmentService


def main():

    print("--- Conectando ao SQL Server ---")
    conn = get_connection()

    try:
        department_service = DepartmentService(conn)
        departments = department_service.get_all_Department()

        print(f"Total de departamentos encontrados: {len(departments)}")
        for dept in departments:
            print(f"- ID: {dept.id} | Nome: {dept.name}")

    finally:
        conn.close()
        print("--- Conexao encerrada com sucesso ---")


if __name__ == "__main__":
    main()