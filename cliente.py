class Cliente:
    """Classe simples para representar um cliente"""
    
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.pedidos = []  # Lista para guardar pedidos do cliente
    
    def adicionar_pedido(self, pedido):
        """Adiciona um pedido à lista do cliente"""
        self.pedidos.append(pedido)
    
    def mostrar_info(self):
        """Mostra informações básicas do cliente"""
        return f"Cliente: {self.nome} | Email: {self.email}"
