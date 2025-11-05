from database import conectar

# =======================================
# RELATÓRIO 1 - Total de Pedidos por Cliente (Agrupamento)
# =======================================
def relatorio_total_pedidos_por_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n📊 Relatório: Total de Pedidos por Cliente\n")

    cursor.execute("""
        SELECT 
            c.nome AS cliente,
            COUNT(p.id_pedido) AS qtd_pedidos,
            COALESCE(SUM(p.total), 0) AS valor_total
        FROM clientes c
        LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente
        GROUP BY c.nome
        ORDER BY c.nome;
    """)

    resultados = cursor.fetchall()

    print(f"{'Cliente':<30}{'Qtd. Pedidos':<15}{'Valor Total (R$)':<15}")
    print("-" * 60)

    for r in resultados:
        print(f"{r[0]:<30}{r[1]:<15}{r[2]:<15.2f}")

    cursor.close()
    conexao.close()


# =======================================
# RELATÓRIO 2 - Itens de Pedidos com Cliente e Produto (Junção)
# =======================================
def relatorio_itens_pedidos_cliente_produto():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n📋 Relatório: Itens dos Pedidos (Cliente + Produto)\n")

    # Consulta corrigida — soma corretamente os subtotais com base na quantidade e preço
    cursor.execute("""
        SELECT 
            ped.id_pedido,
            c.nome AS cliente,
            p.nome AS produto,
            SUM(i.quantidade) AS qtd_total,
            SUM(i.quantidade * p.preco) AS subtotal_corrigido,
            ped.status
        FROM itens_pedidos i
        JOIN pedidos ped ON i.id_pedido = ped.id_pedido
        JOIN clientes c ON ped.id_cliente = c.id_cliente
        JOIN produtos p ON i.id_produto = p.id_produto
        GROUP BY ped.id_pedido, c.nome, p.nome, ped.status
        ORDER BY ped.id_pedido, c.nome;
    """)

    resultados = cursor.fetchall()

    print(f"{'Pedido':<8}{'Cliente':<25}{'Produto':<25}{'Qtd':<5}{'Subtotal(R$)':<15}{'Status':<10}")
    print("-" * 90)

    for r in resultados:
        print(f"{r[0]:<8}{r[1]:<25}{r[2]:<25}{r[3]:<5}{r[4]:<15.2f}{r[5]:<10}")

    cursor.close()
    conexao.close()
