# 🐾 Sistema de Vendas - Pet Shop Amigo Cachorro

**Autor:** Caio Borba da Silva Souza 
**Disciplina:** Banco de Dados 
**Professor:** Howard Cruz

---

## 📘 Descrição do Projeto
Este projeto foi desenvolvido como parte da atividade prática da disciplina de Banco de Dados. 
A aplicação tem como objetivo gerenciar o processo de vendas de um pet shop, permitindo o controle de **clientes**, **produtos**, **pedidos** e **itens de pedidos**.

O sistema foi implementado em **Python**, utilizando o **PostgreSQL** como banco de dados relacional, com execução dentro de uma máquina virtual Linux (VirtualBox).

---

## 🎥 Vídeo de Demonstração

📺 **Link do vídeo:** [Assista no YouTube](https://youtu.be/xEkVrnU3o4o)

---

## 🗂️ Estrutura do Projeto

vendas_online_project/
├── README.md
├── diagramaaa.pdf
├── scripts/
│ └── create_tabelas.sql
├── src/
│ ├── main.py
│ ├── database.py
│ └── controllers/
│ ├── clientes_controller.py
│ ├── produtos_controller.py
│ ├── pedidos_controller.py
│ ├── itens_pedidos_controller.py
│ └── relatorios_controller.py
└── python_app/



---

## ⚙️ Como Executar o Projeto

### 1️⃣ Acesse o diretório do projeto
```bash
cd ~/vendas_online_project/src

2️⃣ Execute o sistema

python3 main.py

3️⃣ O sistema exibirá um menu principal com as seguintes opções:
Clientes

Listar, Inserir, Atualizar, Remover

Produtos

Listar, Inserir, Atualizar, Remover

Pedidos

Listar, Inserir, Atualizar, Remover

Itens dos Pedidos

Listar, Inserir, Atualizar, Remover

Relatórios

Total de Pedidos por Cliente (agrupamento)

Itens de Pedidos com Cliente e Produto (junção)

🧱 Banco de Dados
Banco utilizado: PostgreSQL

Script de criação: scripts/create_tabelas.sql

Banco de dados: vendasdb

Conexão configurada em: src/database.py

Tabelas Principais
clientes — dados dos clientes (nome, email, telefone, endereço)

produtos — catálogo de produtos (nome, descrição, preço, estoque)

pedidos — registros dos pedidos, vinculados aos clientes

itens_pedidos — itens de cada pedido, vinculados aos produtos e pedidos

Todos os relacionamentos entre tabelas estão implementados com chaves estrangeiras (FK) e chaves primárias (PK) corretamente configuradas.

🧩 Diagrama Relacional
O diagrama do banco de dados encontra-se no arquivo diagramaaa.pdf.

Ele apresenta os relacionamentos entre as tabelas:

clientes → pedidos → itens_pedidos → produtos

Definição de 1:N e N:N

Todas as chaves estrangeiras e restrições NOT NULL

💡 Funcionalidades Implementadas
✅ Conexão automática com PostgreSQL
✅ CRUD completo (Create, Read, Update, Delete) para todas as entidades
✅ Atualização automática de estoque e totais de pedido
✅ Relatórios com junções e agrupamentos SQL
✅ Menu interativo no terminal
✅ Organização modular por controllers e camadas de lógica

🧰 Tecnologias Utilizadas
Python 3

PostgreSQL

psycopg2 (conector Python/Postgres)

Ubuntu (Linux) — ambiente de execução

Git & GitHub — versionamento e entrega

🧑‍💻 Como Reproduzir no Seu Ambiente
Clone o repositório:


git clone https://github.com/SEU_USUARIO/vendas_online_project.git
Acesse o projeto:


cd vendas_online_project/src
Configure o banco de dados:

Crie um banco chamado vendasdb no PostgreSQL.

Execute o script:


psql -U seu_usuario -d vendasdb -f ../scripts/create_tabelas.sql
Execute o sistema:


python3 main.py

📂 Repositório
Todos os arquivos estão organizados conforme solicitado:

scripts/ → Criação do banco de dados

src/ → Código-fonte completo

diagramaaa.pdf → Diagrama relacional

README.md → Instruções e documentação

Vídeo explicativo disponível no YouTube
