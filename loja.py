from produto import Produto
from cliente import Cliente
from pedido import Pedido
from carrinho import Carrinho

class Loja:
    """Classe principal que gerencia toda a loja"""
    
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []  # Lista de produtos disponíveis
        self.clientes = []  # Lista de clientes cadastrados
        self.pedidos = []  # Lista de todos os pedidos
        self.ultimo_numero_pedido = 0
        self.carrinho = Carrinho()
    
    def cadastrar_produto(self, nome, preco, estoque):
        """Cadastra um novo produto na loja"""
        novo_id = len(self.produtos) + 1
        produto = Produto(novo_id, nome, preco, estoque)
        self.produtos.append(produto)
        print(f"Produto '{nome}' cadastrado com sucesso!")
        return produto
    
    def cadastrar_cliente(self, nome, email, endereco):
        """Cadastra um novo cliente"""
        cliente = Cliente(nome, email, endereco)
        self.clientes.append(cliente)
        print(f"Cliente '{nome}' cadastrado com sucesso!")
        return cliente
    
    def listar_produtos(self):
        """Mostra todos os produtos disponíveis"""
        print("=== PRODUTOS DISPONÍVEIS ===")
        for produto in self.produtos:
            if produto.estoque > 0:
                print(f"{produto.id}. {produto.mostrar_info()}")
    
    def encontrar_produto(self, produto_id):
        """Encontra um produto pelo ID"""
        for produto in self.produtos:
            if produto.id == produto_id:
                return produto
        return None
    
    def criar_pedido(self, cliente):
        """Cria um novo pedido a partir do carrinho"""
        if not self.carrinho.itens:
            print("Carrinho vazio! Adicione itens primeiro.")
            return None
        
        self.ultimo_numero_pedido += 1
        pedido = Pedido(self.ultimo_numero_pedido, cliente)
        
        # Adiciona todos os itens do carrinho ao pedido
        for produto_id, quantidade in self.carrinho.itens.items():
            produto = self.carrinho.produtos[produto_id]
            pedido.adicionar_item(produto, quantidade)
        
        cliente.adicionar_pedido(pedido)
        self.pedidos.append(pedido)
        self.carrinho.limpar_carrinho()
        
        print("Pedido criado com sucesso!")
        return pedido
    
    def processar_pagamento(self, pedido):
        """Simula o processamento de pagamento"""
        print(f"Processando pagamento do pedido #{pedido.numero}...")
        print(f"Valor total: R${pedido.total:.2f}")
        pedido.mudar_status("Pago")
        print("Pagamento aprovado! Pedido será enviado.")
    
    def menu_principal(self):
        """Menu interativo simples para testar a loja"""
        print(f"=== BEM-VINDO À {self.nome.upper()} ===\n")
        
        # Cadastra um cliente de exemplo
        cliente = self.cadastrar_cliente("João Silva", "joao@email.com", "Rua A, 123 - São Paulo")
        
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Ver produtos")
            print("2. Adicionar ao carrinho")
            print("3. Ver carrinho")
            print("4. Fazer pedido")
            print("5. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.listar_produtos()
            
            elif opcao == "2":
                self.listar_produtos()
                try:
                    produto_id = int(input("Digite o ID do produto: "))
                    quantidade = int(input("Digite a quantidade: "))
                    
                    produto = self.encontrar_produto(produto_id)
                    if produto:
                        self.carrinho.adicionar_item(produto, quantidade)
                    else:
                        print("Produto não encontrado!")
                except ValueError:
                    print("Digite números válidos!")
            
            elif opcao == "3":
                print(self.carrinho.mostrar_carrinho())
            
            elif opcao == "4":
                if self.carrinho.itens:
                    pedido = self.criar_pedido(cliente)
                    if pedido:
                        print(pedido.mostrar_pedido())
                        confirmar = input("Confirmar pedido? (s/n): ")
                        if confirmar.lower() == 's':
                            self.processar_pagamento(pedido)
                else:
                    print("Carrinho vazio!")
            
            elif opcao == "5":
                print("Obrigado por visitar nossa loja!")
                break
            
            else:
                print("Opção inválida!")
