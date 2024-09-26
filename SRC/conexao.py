import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'valadas',
    host = 'localhost',
    password = 'projeto123',
    db = 'Projeto_CRUD'
)

if conn.is_connected():
    print('Conectando com o banco!')
else:
    print('Não foi possivel fazer a conexão!')