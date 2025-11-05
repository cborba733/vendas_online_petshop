import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="vendasdb",
            user="caio",
            password="gmai2015"
        )
        print("Conexão bem-sucedida com o banco de dados!")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None
