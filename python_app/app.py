import psycopg2

# Configuração da conexão com o banco PostgreSQL
DB_CONFIG = {
    "host": "localhost",
    "database": "vendasdb",
    "user": "caio",
    "password": "gmai2015"
}

def conectar():
    """Estabelece conexão com o banco de dados"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco:", e)

# ---------------- CRUD CLIENTES ----------------

def listar_clientes():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers ORDER BY customer_id;")
    clientes = cur.fetchall()
    print("\n--- Lista de Clientes ---")
    for c in clientes:
        print(f"{c[0]} - {c[1]} ({c[2]}) - Tel: {c[3]}")
    cur.close()
    conn.close()

def adicionar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)", (nome, email, telefone))
    conn.commit()
    print("✅ Cliente adicionado com sucesso!")
    cur.close()
    conn.close()

def atualizar_cliente():
    listar_clientes()
    cid = input("Digite o ID do cliente para atualizar: ")
    novo_nome = input("Novo nome: ")
    novo_email = input("Novo email: ")
    novo_tel = input("Novo telefone: ")
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        UPDATE customers 
        SET name=%s, email=%s, phone=%s 
        WHERE customer_id=%s
    """, (novo_nome, novo_email, novo_tel, cid))
    conn.commit()
    print("✅ Cliente atualizado com sucesso!")
    cur.close()
    conn.close()

def deletar_cliente():
    listar_clientes()
    cid = input("Digite o ID do cliente para deletar: ")
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM customers WHERE customer_id=%s", (cid,))
    conn.commit()
    print("✅ Cliente removido com sucesso!")
    cur.close()
    conn.close()

# ---------------- MENU PRINCIPAL ----------------

def menu():
    while True:
        print("\n=== SISTEMA DE VENDAS ONLINE ===")
        print("1 - Listar clientes")
        print("2 - Adicionar cliente")
        print("3 - Atualizar cliente")
        print("4 - Remover cliente")
        print("0 - Sair")
        opc = input("Escolha: ")

        if opc == "1":
            listar_clientes()
        elif opc == "2":
            adicionar_cliente()
        elif opc == "3":
            atualizar_cliente()
        elif opc == "4":
            deletar_cliente()
        elif opc == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
