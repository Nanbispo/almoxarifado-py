from django.db.models.sql import AND

from models.department import Department


class DepartmentService:
    # Queries organizadas na ordem de uso/ações do banco de dados
    QUERY_SELECT = "SELECT ID, NAME FROM DEPARTMENT WHERE D_E_L_E_T_ = '' or D_E_L_E_T_ IS NULL AND DATBLO IS NULL"
    QUERY_SELECT_BY_ID = "SELECT ID, NAME FROM DEPARTMENT WHERE ID = ?"
    QUERY_INSERT = "INSERT INTO DEPARTMENT (NAME) VALUES (?)"
    QUERY_UPDATE = "UPDATE DEPARTMENT SET NAME = ? WHERE ID = ?"
    QUERY_DELET = "UPDATE DEPARTMENT SET D_E_L_E_T_ = '*' WHERE ID = ?"

    def __init__(self, connection):
        """
        Inicializa o serviço recebendo a conexão com o banco de dados.
        """
        self.connection = connection

    def get_all_Department(self) -> list[Department]:
        """
        Executa a query: SELECT ID, NAME FROM DEPARTMENT
        Retorna a lista de objetos Department mantendo a ordem das colunas (ID, NAME).
        """
        cursor = self.connection.cursor()
        cursor.execute(self.QUERY_SELECT)
        rows = cursor.fetchall()
        # id = row[0], name = row[1] conforme a ordem do SELECT
        return [Department(id=row[0], name=row[1]) for row in rows]

    def get_by_id_Department(self, id: int) -> Department | None:
        """
        Executa a busca por ID: SELECT ID, NAME FROM DEPARTMENT WHERE ID = ?
        """
        cursor = self.connection.cursor()
        cursor.execute(self.QUERY_SELECT_BY_ID, (id,))
        row = cursor.fetchone()
        if row:
            return Department(id=row[0], name=row[1])
        return None

    def insert_Department(self, name: str) -> None:
        """
        Executa a query: INSERT INTO DEPARTMENT (NAME) VALUES (?)
        Insere um novo departamento informando o NAME (ID é gerado via IDENTITY).
        """
        cursor = self.connection.cursor()
        cursor.execute(self.QUERY_INSERT, (name,))
        self.connection.commit()

    def update_Department(self, id: int, name: str) -> None:
        """
        Executa a query de atualização (que faltava):
        UPDATE DEPARTMENT SET NAME = ? WHERE ID = ?
        """
        cursor = self.connection.cursor()
        cursor.execute(self.QUERY_UPDATE, (name, id))
        self.connection.commit()

    def delet_Department(self, id: int) -> None:
        cursor = self.connection.cursor()
        cursor.execute(self.QUERY_DELET, (id,))
        self.connection.commit()
