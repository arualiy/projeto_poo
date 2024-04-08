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
        super()._init_(nome, preco)
        self.tamanho = tamanho

    def exibir_info(self):
        return super().exibir_info() + f" | Tamanho: {self.tamanho}"

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)

    def exibir_produtos(self):
        return [produto.exibir_info() for produto in self.produtos]

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = CarrinhoDeCompras()

    @st.cache(allow_output_mutation=True)
    def get_carrinho(self):
        return self.carrinho

nome_cliente = st.sidebar.text_input("Qual é o seu nome?", "Nome do Cliente")
cliente = Cliente(nome_cliente)
carrinho = cliente.get_carrinho()

tipo_produto = st.selectbox("Selecione o tipo de produto", ["Eletrônico", "Vestuário"])

if tipo_produto == "Eletrônico":
    produto_selecionado = st.selectbox("Selecione o produto eletrônico",
                                        [("Smartphone", 2000, "Samsung"),
                                            ("Notebook", 3500, "Dell"),
                                            ("Computador", 5000, "Lenovo")])
elif tipo_produto == "Vestuário":
    produto_selecionado = st.selectbox("Selecione o produto de vestuário",
                                        [("Camiseta", 29.99, "M"),
                                         ("Calça Jeans", 59.99, "38")])

nome, preco, caracteristica = produto_selecionado
if tipo_produto == "Eletrônico":
    produto = ProdutoEletronico(nome, preco, caracteristica)
else:
    produto = ProdutoVestuario(nome, preco, caracteristica)

if st.button("Adicionar ao Carrinho"):
    carrinho.adicionar_produto(produto)

st.write("Produtos no Carrinho")
for produto_info in carrinho.exibir_produtos():
    st.write(produto_info)

st.write(f"Total: R${carrinho.calcular_total():.2f}")
