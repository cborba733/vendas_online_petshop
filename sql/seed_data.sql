-- Inserindo clientes
INSERT INTO clientes (nome, email, telefone, endereco) VALUES
('Caio Borba da Silva Souza', 'caio@example.com', '27999990001', 'Rua das Palmeiras, 123'),
('João Mendes', 'joao@example.com', '27999990002', 'Av. Central, 456'),
('Maria Oliveira', 'maria@example.com', '27999990003', 'Rua das Flores, 789');

-- Inserindo produtos
INSERT INTO produtos (nome, descricao, preco, estoque) VALUES
('Ração Premium 10kg', 'Ração completa para cães adultos', 150.00, 25),
('Coleira Antipulgas', 'Coleira de 60 dias de proteção', 89.90, 50),
('Brinquedo Bola', 'Bola de borracha para pets', 25.00, 100),
('Shampoo Neutro 500ml', 'Shampoo para todos os tipos de pelos', 35.00, 40),
('Petisco Natural 200g', 'Petisco saudável sabor frango', 20.00, 60);

-- Inserindo pedidos
INSERT INTO pedidos (id_cliente, data_pedido, total, status) VALUES
(1, CURRENT_DATE, 150.00, 'Pago'),
(2, CURRENT_DATE, 115.00, 'Pendente');

-- Inserindo itens dos pedidos
INSERT INTO itens_pedidos (id_pedido, id_produto, quantidade, subtotal) VALUES
(1, 1, 1, 150.00),
(2, 2, 1, 89.90),
(2, 5, 1, 20.00),
(2, 3, 2, 25.00);
