import os
import pyodbc
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()


def get_connection() -> pyodbc.Connection:
    """
    Cria e retorna uma conexão com o banco de dados SQL Server
    utilizando as configurações definidas no arquivo .env ou padrões locais.
    """
    driver = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")
    server = os.getenv("DB_SERVER", "localhost")
    database = os.getenv("DB_NAME", "ALMOXARIFADO_PY")
    trusted_connection = os.getenv("DB_TRUSTED_CONNECTION", "yes")
    trust_server_certificate = os.getenv("DB_TRUST_SERVER_CERTIFICATE", "yes")

    connection_string = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection={trusted_connection};"
        f"TrustServerCertificate={trust_server_certificate};"
    )

    try:
        connection = pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as error:
        print(f"Erro ao conectar com o banco de dados SQL Server: {error}")
        raise
