# 🛒 Simulador de Loja Online em Python

Um sistema de e-commerce simples desenvolvido em Python usando Programação Orientada a Objetos (POO).

## 📁 Estrutura do Projeto

```
ecommerce/
├── main.py          # Arquivo principal que inicia a loja
├── produto.py       # Classe Produto - representa os itens à venda
├── cliente.py       # Classe Cliente - representa os compradores
├── pedido.py        # Classe Pedido - gerencia os pedidos
├── carrinho.py      # Classe Carrinho - gerencia o carrinho de compras
└── loja.py          # Classe Loja - sistema principal que coordena tudo
```

## 🎯 Conceitos de POO Utilizados

- **Classes e Objetos**
- **Encapsulamento** (atributos e métodos)
- **Métodos especiais** (__init__, __str__)
- **Composição** (um objeto contém outros objetos)
- **Métodos de instância**

## 📋 Classes e Suas Funções

### 1. 🏷️ Classe Produto (`produto.py`)

**O que representa:** Cada produto à venda na loja

**Atributos:**
- `id` - número único para identificar o produto
- `nome` - nome do produto (ex: "Camiseta")
- `preco` - preço em reais (ex: 29.90)
- `estoque` - quantidade disponível

**Métodos principais:**
- `mostrar_info()` - exibe informações do produto
- `vender(quantidade)` - reduz o estoque quando vendido

**Exemplo de uso:**
```python
camiseta = Produto(1, "Camiseta", 29.90, 50)
print(camiseta.mostrar_info())  # Camiseta - R$29.90 (50 em estoque)
```

---

### 2. 👤 Classe Cliente (`cliente.py`)

**O que representa:** Uma pessoa que compra na loja

**Atributos:**
- `nome` - nome do cliente
- `email` - email para contato
- `endereco` - endereço de entrega
- `pedidos` - lista de pedidos feitos

**Métodos principais:**
- `adicionar_pedido(pedido)` - guarda o histórico de compras
- `mostrar_info()` - exibe dados do cliente

**Exemplo de uso:**
```python
joao = Cliente("João", "joao@email.com", "Rua A, 123")
print(joao.mostrar_info())  # Cliente: João | Email: joao@email.com
```

---

### 3. 📦 Classe Pedido (`pedido.py`)

**Contém duas classes:**
- `ItemPedido` - um item específico no pedido
- `Pedido` - o pedido completo

**ItemPedido - Atributos:**
- `produto` - qual produto foi comprado
- `quantidade` - quantas unidades
- `preco_total` - preço × quantidade

**Pedido - Atributos:**
- `numero` - número único do pedido
- `cliente` - quem fez o pedido
- `itens` - lista de itens comprados
- `total` - valor total do pedido
- `status` - situação do pedido

**Métodos principais:**
- `adicionar_item(produto, quantidade)` - adiciona um item
- `mostrar_pedido()` - exibe detalhes do pedido
- `mudar_status(novo_status)` - atualiza o status

**Exemplo de uso:**
```python
pedido = Pedido(1, joao)
pedido.adicionar_item(camiseta, 2)
print(pedido.mostrar_pedido())
```

---

### 4. 🛒 Classe Carrinho (`carrinho.py`)

**O que representa:** Carrinho de compras temporário

**Atributos:**
- `itens` - dicionário {id_produto: quantidade}
- `produtos` - referência aos objetos produto

**Métodos principais:**
- `adicionar_item(produto, quantidade)` - coloca produto no carrinho
- `remover_item(produto_id)` - tira produto do carrinho
- `mostrar_carrinho()` - exibe itens e total
- `calcular_total()` - calcula o valor total

**Exemplo de uso:**
```python
carrinho = Carrinho()
carrinho.adicionar_item(camiseta, 2)
print(carrinho.mostrar_carrinho())
```

---

### 5. 🏪 Classe Loja (`loja.py`)

**O que representa:** O sistema principal da loja

**Atributos:**
- `produtos` - lista de produtos cadastrados
- `clientes` - lista de clientes cadastrados
- `pedidos` - histórico de todos os pedidos
- `carrinho` - carrinho atual

**Métodos principais:**
- `cadastrar_produto()` - adiciona novo produto
- `cadastrar_cliente()` - registra novo cliente
- `listar_produtos()` - mostra produtos disponíveis
- `criar_pedido()` - transforma carrinho em pedido
- `menu_principal()` - menu interativo

---

## 🚀 Como Executar

1. **Baixe todos os arquivos** em uma pasta
2. **Execute o arquivo principal**:
   ```bash
   python main.py
   ```

3. **Siga o menu interativo**:
   - 1️⃣ Ver produtos disponíveis
   - 2️⃣ Adicionar produtos ao carrinho
   - 3️⃣ Ver carrinho
   - 4️⃣ Fazer pedido
   - 5️⃣ Sair

---

## 💡 Dicas para Estudo

1. **Comece pela classe Produto** - é a mais simples
2. **Teste cada classe separadamente** antes de integrar
3. **Modifique valores** para ver como o sistema se comporta
4. **Adicione novos recursos** como desconto ou frete
5. **Tente criar uma nova classe** (ex: Categoria, Fornecedor)

---

## 🔥 Achou fácil?

Aqui estão algumas melhorias que podem ser implementadas:
- [ ] Sistema de login para clientes
- [ ] Categorias de produtos
- [ ] Sistema de descontos e promoções
- [ ] Histórico de pedidos por cliente
- [ ] Salvar dados em arquivo
- [ ] Interface gráfica

---

## 📚 Glossário de POO

- **Classe**: "Molde" para criar objetos
- **Objeto**: Instância de uma classe
- **Atributo**: Característica do objeto
- **Método**: Ação que o objeto pode fazer
- **Encapsulamento**: Agrupar dados e comportamentos
- **Composição**: Um objeto conter outros objetos

---

Divirta-se programando! 🐍✨

*Feio com ❤️ pelo professor Lucas*
