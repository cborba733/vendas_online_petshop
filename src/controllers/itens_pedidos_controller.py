from database import conectar

# =======================================
# LISTAR ITENS
# =======================================
def listar_itens_pedidos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT i.id_item_pedido, p.nome AS produto, ped.id_pedido, i.quantidade, i.subtotal
        FROM itens_pedidos i
        JOIN produtos p ON i.id_produto = p.id_produto
        JOIN pedidos ped ON i.id_pedido = ped.id_pedido
        ORDER BY i.id_item_pedido;
    """)
    itens = cursor.fetchall()

    print("\n--- Itens dos Pedidos ---")
    for i in itens:
        print(f"ID Item: {i[0]} | Produto: {i[1]} | Pedido: {i[2]} | Quantidade: {i[3]} | Subtotal: R${i[4]:.2f}")

    cursor.close()
    conexao.close()


# =======================================
# INSERIR ITEM
# =======================================
def inserir_item_pedido():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n--- Inserir Item em Pedido ---")

    # Mostrar pedidos disponíveis
    cursor.execute("SELECT id_pedido, total FROM pedidos ORDER BY id_pedido;")
    pedidos = cursor.fetchall()
    for ped in pedidos:
        print(f"{ped[0]} - Pedido (Total atual: R${ped[1]:.2f})")

    id_pedido = input("Digite o ID do pedido: ")

    # Verificar se o pedido existe
    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE id_pedido = %s;", (id_pedido,))
    if cursor.fetchone()[0] == 0:
        print("⚠️ Pedido não encontrado! Escolha um ID válido.")
        cursor.close()
        conexao.close()
        return

    # Mostrar produtos disponíveis
    cursor.execute("SELECT id_produto, nome, preco, estoque FROM produtos ORDER BY id_produto;")
    produtos = cursor.fetchall()
    for prod in produtos:
        print(f"{prod[0]} - {prod[1]} (Preço: R${prod[2]:.2f}, Estoque: {prod[3]})")

    id_produto = input("Digite o ID do produto: ")

    # Verificar se o produto existe
    cursor.execute("SELECT preco, estoque FROM produtos WHERE id_produto = %s;", (id_produto,))
    produto = cursor.fetchone()
    if not produto:
        print("⚠️ Produto não encontrado!")
        cursor.close()
        conexao.close()
        return

    preco, estoque_atual = produto
    quantidade = int(input("Quantidade: "))

    # Verificar estoque
    if quantidade > estoque_atual:
        print(f"⚠️ Estoque insuficiente! Estoque atual: {estoque_atual}")
        cursor.close()
        conexao.close()
        return

    subtotal = preco * quantidade

    # ⚙️ Verifica se o produto já existe no mesmo pedido
    cursor.execute("""
        SELECT id_item_pedido, quantidade, subtotal
        FROM itens_pedidos
        WHERE id_pedido = %s AND id_produto = %s;
    """, (id_pedido, id_produto))
    existente = cursor.fetchone()

    if existente:
        # Atualiza a quantidade e o subtotal
        id_item, qtd_atual, subtotal_atual = existente
        nova_qtd = qtd_atual + quantidade
        novo_subtotal = subtotal_atual + subtotal

        cursor.execute("""
            UPDATE itens_pedidos
            SET quantidade = %s, subtotal = %s
            WHERE id_item_pedido = %s;
        """, (nova_qtd, novo_subtotal, id_item))
    else:
        # Insere novo item
        cursor.execute("""
            INSERT INTO itens_pedidos (id_pedido, id_produto, quantidade, subtotal)
            VALUES (%s, %s, %s, %s)
        """, (id_pedido, id_produto, quantidade, subtotal))

    # Atualizar total do pedido
    cursor.execute("""
        UPDATE pedidos
        SET total = (
            SELECT SUM(subtotal) FROM itens_pedidos WHERE id_pedido = %s
        )
        WHERE id_pedido = %s;
    """, (id_pedido, id_pedido))

    # Atualizar estoque do produto
    cursor.execute("""
        UPDATE produtos
        SET estoque = estoque - %s
        WHERE id_produto = %s;
    """, (quantidade, id_produto))

    conexao.commit()
    print(f"✅ Item inserido/atualizado com sucesso! Subtotal: R${subtotal:.2f}")

    cursor.close()
    conexao.close()


# =======================================
# ATUALIZAR ITEM
# =======================================
def atualizar_item_pedido():
    conexao = conectar()
    cursor = conexao.cursor()

    listar_itens_pedidos()
    id_item = input("\nDigite o ID do item a atualizar: ")

    nova_qtd = int(input("Nova quantidade: "))

    # Buscar preço e recalcular subtotal
    cursor.execute("""
        SELECT id_produto, id_pedido FROM itens_pedidos WHERE id_item_pedido = %s
    """, (id_item,))
    resultado = cursor.fetchone()

    if not resultado:
        print("⚠️ Item não encontrado!")
        cursor.close()
        conexao.close()
        return

    id_produto, id_pedido = resultado

    cursor.execute("SELECT preco FROM produtos WHERE id_produto = %s", (id_produto,))
    preco = cursor.fetchone()[0]
    novo_subtotal = preco * nova_qtd

    # Atualizar subtotal e quantidade
    cursor.execute("""
        UPDATE itens_pedidos
        SET quantidade=%s, subtotal=%s
        WHERE id_item_pedido=%s
    """, (nova_qtd, novo_subtotal, id_item))

    # Atualizar total do pedido
    cursor.execute("""
        UPDATE pedidos
        SET total = (
            SELECT SUM(subtotal) FROM itens_pedidos WHERE id_pedido = %s
        )
        WHERE id_pedido = %s
    """, (id_pedido, id_pedido))

    conexao.commit()
    print("✅ Item do pedido atualizado com sucesso!")
    cursor.close()
    conexao.close()


# =======================================
# REMOVER ITEM
# =======================================
def remover_item_pedido():
    conexao = conectar()
    cursor = conexao.cursor()

    listar_itens_pedidos()
    id_item = input("\nDigite o ID do item a remover: ")

    # Pegar subtotal antes de deletar (para atualizar o total do pedido)
    cursor.execute("""
        SELECT subtotal, id_pedido, id_produto, quantidade 
        FROM itens_pedidos 
        WHERE id_item_pedido = %s
    """, (id_item,))
    resultado = cursor.fetchone()

    if not resultado:
        print("⚠️ Item não encontrado!")
        cursor.close()
        conexao.close()
        return

    subtotal, id_pedido, id_produto, quantidade = resultado

    # Remover item
    cursor.execute("DELETE FROM itens_pedidos WHERE id_item_pedido = %s", (id_item,))

    # Atualizar total do pedido
    cursor.execute("""
        UPDATE pedidos
        SET total = total - %s
        WHERE id_pedido = %s
    """, (subtotal, id_pedido))

    # Devolver o estoque do produto removido
    cursor.execute("""
        UPDATE produtos
        SET estoque = estoque + %s
        WHERE id_produto = %s
    """, (quantidade, id_produto))

    conexao.commit()
    print("🗑️ Item removido com sucesso e total do pedido atualizado!")

    cursor.close()
    conexao.close()

