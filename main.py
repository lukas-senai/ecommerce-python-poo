from loja import Loja

def main():
    """Função principal para executar a loja"""
    # Cria uma nova loja
    minha_loja = Loja("Loja do Python")

    # Cadastra alguns produtos
    minha_loja.cadastrar_produto("Camiseta", 29.90, 50)
    minha_loja.cadastrar_produto("Calça Jeans", 89.90, 30)
    minha_loja.cadastrar_produto("Tênis", 129.90, 20)
    minha_loja.cadastrar_produto("Boné", 25.00, 40)
    
    # Inicia o menu interativo
    minha_loja.menu_principal()

# Executa o programa
if __name__ == "__main__":
    main()
