class Produto:
    """Classe simples para representar um produto"""
    
    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def mostrar_info(self):
        """Mostra informações do produto de forma simples"""
        return f"{self.nome} - R${self.preco:.2f} ({self.estoque} em estoque)"
    
    def vender(self, quantidade):
        """Diminui o estoque quando o produto é vendido"""
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print("Estoque insuficiente!")
            return False
