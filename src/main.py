from controllers.clientes_controller import (
    listar_clientes,
    inserir_cliente,
    atualizar_cliente,
    remover_cliente
)
from controllers.produtos_controller import (
    listar_produtos,
    inserir_produto,
    atualizar_produto,
    remover_produto
)
from controllers.pedidos_controller import (
    listar_pedidos,
    inserir_pedido,
    atualizar_pedido,
    remover_pedido
)
from controllers.itens_pedidos_controller import (
    listar_itens_pedidos,
    inserir_item_pedido,
    atualizar_item_pedido,
    remover_item_pedido
)
from controllers.relatorios_controller import (
    relatorio_total_pedidos_por_cliente,
    relatorio_itens_pedidos_cliente_produto
)

# ==================================================
# FUNÇÕES DE MENU
# ==================================================
def menu_clientes():
    while True:
        print("\n=== MENU CLIENTES ===")
        print("1 - Listar Clientes")
        print("2 - Inserir Cliente")
        print("3 - Atualizar Cliente")
        print("4 - Remover Cliente")
        print("0 - Voltar")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            listar_clientes()
        elif opc == "2":
            inserir_cliente()
        elif opc == "3":
            atualizar_cliente()
        elif opc == "4":
            remover_cliente()
        elif opc == "0":
            break
        else:
            print("❌ Opção inválida!")


def menu_produtos():
    while True:
        print("\n=== MENU PRODUTOS ===")
        print("1 - Listar Produtos")
        print("2 - Inserir Produto")
        print("3 - Atualizar Produto")
        print("4 - Remover Produto")
        print("0 - Voltar")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            listar_produtos()
        elif opc == "2":
            inserir_produto()
        elif opc == "3":
            atualizar_produto()
        elif opc == "4":
            remover_produto()
        elif opc == "0":
            break
        else:
            print("❌ Opção inválida!")


def menu_pedidos():
    while True:
        print("\n=== MENU PEDIDOS ===")
        print("1 - Listar Pedidos")
        print("2 - Inserir Pedido")
        print("3 - Atualizar Pedido")
        print("4 - Remover Pedido")
        print("0 - Voltar")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            listar_pedidos()
        elif opc == "2":
            inserir_pedido()
        elif opc == "3":
            atualizar_pedido()
        elif opc == "4":
            remover_pedido()
        elif opc == "0":
            break
        else:
            print("❌ Opção inválida!")


def menu_itens_pedidos():
    while True:
        print("\n=== MENU ITENS DOS PEDIDOS ===")
        print("1 - Listar Itens")
        print("2 - Inserir Item em Pedido")
        print("3 - Atualizar Item de Pedido")
        print("4 - Remover Item de Pedido")
        print("0 - Voltar")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            listar_itens_pedidos()
        elif opc == "2":
            inserir_item_pedido()
        elif opc == "3":
            atualizar_item_pedido()
        elif opc == "4":
            remover_item_pedido()
        elif opc == "0":
            break
        else:
            print("❌ Opção inválida!")


def menu_relatorios():
    while True:
        print("\n=== MENU RELATÓRIOS ===")
        print("1 - Total de Pedidos por Cliente (Agrupamento)")
        print("2 - Itens de Pedidos com Cliente e Produto (Junção)")
        print("0 - Voltar")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            relatorio_total_pedidos_por_cliente()
        elif opc == "2":
            relatorio_itens_pedidos_cliente_produto()
        elif opc == "0":
            break
        else:
            print("❌ Opção inválida!")


# ==================================================
# MENU PRINCIPAL
# ==================================================
def menu_principal():
    print("\n=====================================")
    print("💻 SISTEMA DE VENDAS - PET SHOP AMIGO CACHORRO")
    print("Desenvolvido por: Caio Borba da Silva Souza")
    print("=====================================")

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Clientes")
        print("2 - Produtos")
        print("3 - Pedidos")
        print("4 - Itens dos Pedidos")
        print("5 - Relatórios")
        print("0 - Sair")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            menu_clientes()
        elif opc == "2":
            menu_produtos()
        elif opc == "3":
            menu_pedidos()
        elif opc == "4":
            menu_itens_pedidos()
        elif opc == "5":
            menu_relatorios()
        elif opc == "0":
            print("👋 Encerrando o sistema. Até mais!")
            break
        else:
            print("❌ Opção inválida!")


# ==================================================
# EXECUÇÃO
# ==================================================
if __name__ == "__main__":
    menu_principal()
