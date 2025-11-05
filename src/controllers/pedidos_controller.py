from database import conectar
from datetime import date

def listar_pedidos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT p.id_pedido, c.nome AS cliente, p.data_pedido, p.total, p.status
        FROM pedidos p
        JOIN clientes c ON p.id_cliente = c.id_cliente
        ORDER BY p.id_pedido;
    """)
    pedidos = cursor.fetchall()

    print("\n--- Lista de Pedidos ---")
    for p in pedidos:
        print(f"ID: {p[0]} | Cliente: {p[1]} | Data: {p[2]} | Total: R${p[3]:.2f} | Status: {p[4]}")

    cursor.close()
    conexao.close()


def inserir_pedido():
    conexao = conectar()
    cursor = conexao.cursor()

    # Exibir clientes disponíveis
    print("\n--- Inserir Pedido ---")
    cursor.execute("SELECT id_cliente, nome FROM clientes;")
    clientes = cursor.fetchall()
    for c in clientes:
        print(f"{c[0]} - {c[1]}")

    id_cliente = input("Digite o ID do cliente: ")
    total = float(input("Valor total do pedido (R$): "))
    status = input("Status do pedido (Pago / Pendente / Cancelado): ")

    # Adiciona a data atual automaticamente
    data_pedido = date.today()

    cursor.execute(
        "INSERT INTO pedidos (id_cliente, data_pedido, total, status) VALUES (%s, %s, %s, %s)",
        (id_cliente, data_pedido, total, status)
    )

    conexao.commit()
    print("✅ Pedido inserido com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_pedido():
    conexao = conectar()
    cursor = conexao.cursor()
    id_pedido = input("ID do pedido a atualizar: ")

    novo_total = float(input("Novo valor total: "))
    novo_status = input("Novo status (Pago / Pendente / Cancelado): ")

    cursor.execute("""
        UPDATE pedidos
        SET total=%s, status=%s
        WHERE id_pedido=%s
    """, (novo_total, novo_status, id_pedido))

    conexao.commit()
    print("✅ Pedido atualizado com sucesso!")
    cursor.close()
    conexao.close()


def remover_pedido():
    conexao = conectar()
    cursor = conexao.cursor()
    id_pedido = input("ID do pedido a remover: ")
    cursor.execute("DELETE FROM pedidos WHERE id_pedido=%s", (id_pedido,))
    conexao.commit()
    print("🗑️ Pedido removido com sucesso!")
    cursor.close()
    conexao.close()
