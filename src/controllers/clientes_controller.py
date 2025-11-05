from database import conectar

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_cliente, nome, email, telefone, endereco FROM clientes;")
    clientes = cursor.fetchall()
    print("\n--- Lista de Clientes ---")
    for c in clientes:
        print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]} | Telefone: {c[3]} | Endereço: {c[4]}")
    cursor.close()
    conexao.close()


def inserir_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    cursor.execute(
        "INSERT INTO clientes (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)",
        (nome, email, telefone, endereco)
    )
    conexao.commit()
    print("✅ Cliente inserido com sucesso!")
    cursor.close()
    conexao.close()


def atualizar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    id_cliente = input("ID do cliente a atualizar: ")
    novo_nome = input("Novo nome: ")
    novo_email = input("Novo email: ")
    novo_telefone = input("Novo telefone: ")
    novo_endereco = input("Novo endereço: ")

    cursor.execute("""
        UPDATE clientes
        SET nome=%s, email=%s, telefone=%s, endereco=%s
        WHERE id_cliente=%s
    """, (novo_nome, novo_email, novo_telefone, novo_endereco, id_cliente))
    conexao.commit()
    print("✅ Cliente atualizado com sucesso!")
    cursor.close()
    conexao.close()


def remover_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    id_cliente = input("ID do cliente a remover: ")
    cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (id_cliente,))
    conexao.commit()
    print("🗑️ Cliente removido com sucesso!")
    cursor.close()
    conexao.close()
