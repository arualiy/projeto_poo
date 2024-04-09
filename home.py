# Importações
import streamlit as st
from abc import ABC, abstractmethod

# Interface para Produtos
class IProduto(ABC):
    @abstractmethod
    def exibir_info(self):
        pass

class Produto(IProduto):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_info(self):
        return f"Produto: {self.nome} | Preço: R${self.preco:.2f}"

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self.marca = marca

    def exibir_info(self):
        return super().exibir_info() + f" | Marca: {self.marca}"

class ProdutoVestuario(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def exibir_info(self):
        return super().exibir_info() + f" | Tamanho: {self.tamanho}"

class ProdutoEnxoval(Produto):
    def __init__(self, nome, preco, tipo):
        super().__init__(nome, preco)
        self.tipo = tipo

    def exibir_info(self):
        return super().exibir_info() + f" | Tipo: {self.tipo}"

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)

    def exibir_produtos(self):
        return [produto.exibir_info() for produto in self.produtos]

# Decorador para fazer cache da função
@st.cache(allow_output_mutation=True)
def get_carrinho(nome_cliente):
    return CarrinhoDeCompras()

# Nome da loja
nome_loja = "Essência Marketplace"

# Título da página
st.title(nome_loja)

# Solicitando o nome do cliente através de um input na barra lateral
nome_cliente = st.sidebar.text_input("Qual é o seu nome?")
# Obtendo o carrinho do cliente
carrinho = get_carrinho(nome_cliente)

# Selecionando o tipo de produto através de um selectbox
tipo_produto = st.selectbox("Selecione o tipo de produto", ["Eletrônico", "Vestuário", "Enxoval"])

# Condições para selecionar o produto com base no tipo escolhido
if tipo_produto == "Eletrônico":
    # Seleção de produto eletrônico
    produto_selecionado = st.selectbox("Selecione o produto eletrônico",
                                        [("Smartphone", 2000, "Samsung"),
                                         ("Notebook", 3500, "Dell"),
                                         ("Computador", 5000, "Lenovo"),
                                         ("Fone de Ouvido", 50, "AKG"),
                                         ("Tablet", 800, "Apple"),
                                         ("Mouse", 30, "Logitech")])
elif tipo_produto == "Vestuário":
    # Seleção de produto de vestuário
    produto_selecionado = st.selectbox("Selecione o produto de vestuário",
                                        [("Camiseta", 29.99, "M"),
                                         ("Calça Jeans", 59.99, "38"),
                                         ("Vestido", 79.99, "P"),
                                         ("Blusa", 39.99, "G"),
                                         ("Moletom", 49.99, "GG"),
                                         ("Shorts", 35.99, "P")])
elif tipo_produto == "Enxoval":
    # Seleção de produto de enxoval
    produto_selecionado = st.selectbox("Selecione o produto de enxoval",
                                        [("Jogo de Cama", 99.99, "Casal"),
                                         ("Toalha de Banho", 19.99, "Grande"),
                                         ("Cobertor", 79.99, "Queen"),
                                         ("Travesseiro", 29.99, "Almofada"),
                                         ("Cortina", 49.99, "2m x 2m"),
                                         ("Tapete", 39.99, "Pequeno")])

nome, preco, caracteristica = produto_selecionado
# Instanciando o objeto do produto selecionado com base no tipo
if tipo_produto == "Eletrônico":
    produto = ProdutoEletronico(nome, preco, caracteristica)
elif tipo_produto == "Vestuário":
    produto = ProdutoVestuario(nome, preco, caracteristica)
else:
    produto = ProdutoEnxoval(nome, preco, caracteristica)

# Adicionando o produto ao carrinho quando o botão é clicado
if st.button(f"Adicionar ao Carrinho"):
    carrinho.adicionar_produto(produto)

# Exibindo os produtos no carrinho do cliente
st.write(f"Carrinho de {nome_cliente}")
for produto_info in carrinho.exibir_produtos():
    st.write(produto_info)

# Exibindo o total do carrinho
st.write(f"Total: R${carrinho.calcular_total():.2f}")

# Mensagem de agradecimento
if carrinho.produtos:
    st.write(f"Obrigado por comprar na nossa loja! Volte sempre na {nome_loja}!")
