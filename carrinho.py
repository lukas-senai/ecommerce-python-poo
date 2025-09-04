class Carrinho:
    """Classe simples para representar o carrinho de compras"""
    
    def __init__(self):
        self.itens = {}  # {produto_id: quantidade}
        self.produtos = {}  # Referência aos objetos produto
    
    def adicionar_item(self, produto, quantidade=1):
        """Adiciona um produto ao carrinho"""
        if produto.id in self.itens:
            self.itens[produto.id] += quantidade
        else:
            self.itens[produto.id] = quantidade
            self.produtos[produto.id] = produto
        
        print(f"Adicionado {quantidade}x {produto.nome} ao carrinho!")
    
    def remover_item(self, produto_id, quantidade=1):
        """Remove ou diminui a quantidade de um item"""
        if produto_id in self.itens:
            if self.itens[produto_id] <= quantidade:
                del self.itens[produto_id]
                del self.produtos[produto_id]
                print("Item removido do carrinho!")
            else:
                self.itens[produto_id] -= quantidade
                print(f"Quantidade reduzida para {self.itens[produto_id]}")
        else:
            print("Produto não está no carrinho!")
    
    def mostrar_carrinho(self):
        """Mostra todos os itens do carrinho"""
        if not self.itens:
            return "Carrinho vazio!"
        
        info = "=== CARRINHO DE COMPRAS ===\n"
        total = 0
        
        for produto_id, quantidade in self.itens.items():
            produto = self.produtos[produto_id]
            preco_item = produto.preco * quantidade
            total += preco_item
            info += f"{quantidade}x {produto.nome} - R${preco_item:.2f}\n"
        
        info += f"TOTAL: R${total:.2f}"
        return info
    
    def limpar_carrinho(self):
        """Esvazia o carrinho"""
        self.itens.clear()
        self.produtos.clear()
        print("Carrinho limpo!")
    
    def calcular_total(self):
        """Calcula o total do carrinho"""
        total = 0
        for produto_id, quantidade in self.itens.items():
            produto = self.produtos[produto_id]
            total += produto.preco * quantidade
        return total
