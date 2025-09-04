class ItemPedido:
    """Classe para representar um item no pedido"""
    
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_total = produto.preco * quantidade
    
    def mostrar_item(self):
        """Mostra informações do item"""
        return f"{self.quantidade}x {self.produto.nome} - R${self.preco_total:.2f}"

class Pedido:
    """Classe para representar um pedido completo"""
    
    def __init__(self, numero_pedido, cliente):
        self.numero = numero_pedido
        self.cliente = cliente
        self.itens = []  # Lista de itens no pedido
        self.total = 0
        self.status = "Pendente"  # Pendente, Pago, Enviado, Entregue
    
    def adicionar_item(self, produto, quantidade):
        """Adiciona um item ao pedido"""
        if produto.vender(quantidade):
            item = ItemPedido(produto, quantidade)
            self.itens.append(item)
            self.total += item.preco_total
            return True
        return False
    
    def mostrar_pedido(self):
        """Mostra detalhes do pedido"""
        info = f"Pedido #{self.numero} - Status: {self.status}\n"
        info += f"Cliente: {self.cliente.nome}\n"
        info += "Itens:\n"
        
        for item in self.itens:
            info += f"  - {item.mostrar_item()}\n"
        
        info += f"Total: R${self.total:.2f}"
        return info
    
    def mudar_status(self, novo_status):
        """Muda o status do pedido"""
        self.status = novo_status
        print(f"Status do pedido #{self.numero} alterado para: {novo_status}")
