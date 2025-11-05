from database import conectar

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_produto, nome, descricao, preco, estoque FROM produtos;")
    produtos = cursor.fetchall()

    print("\n--- Lista de Produtos ---")
    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Descrição: {p[2]} | Preço: R${p[3]:.2f} | Estoque: {p[4]}")
    
    cursor.close()
    conexao.close()


def inserir_produto():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    preco = float(input("Preço: "))
    estoque = int(input("Quantidade em estoque: "))

    cursor.execute(
        "INSERT INTO produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)",
        (nome, descricao, preco, estoque)
    )
    conexao.commit()
    print("✅ Produto inserido com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_produto():
    conexao = conectar()
    cursor = conexao.cursor()
    id_produto = input("ID do produto a atualizar: ")

    nome = input("Novo nome: ")
    descricao = input("Nova descrição: ")
    preco = float(input("Novo preço: "))
    estoque = int(input("Novo estoque: "))

    cursor.execute("""
        UPDATE produtos
        SET nome=%s, descricao=%s, preco=%s, estoque=%s
        WHERE id_produto=%s
    """, (nome, descricao, preco, estoque, id_produto))

    conexao.commit()
    print("✅ Produto atualizado com sucesso!")

    cursor.close()
    conexao.close()


def remover_produto():
    conexao = conectar()
    cursor = conexao.cursor()
    id_produto = input("ID do produto a remover: ")

    cursor.execute("DELETE FROM produtos WHERE id_produto=%s", (id_produto,))
    conexao.commit()
    print("🗑️ Produto removido com sucesso!")

    cursor.close()
    conexao.close()
