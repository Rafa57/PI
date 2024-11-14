from datetime import datetime

# Definição de Estrutura de Dados
class Categoria:
    def __init__(self, nome: str):
        self.nome = nome

class Produto:
    def __init__(self, id_produto: int, nome: str, categoria: Categoria, preco: float, quantidade: int):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

class Movimentacao:
    def __init__(self, id_produto: int, tipo: str, quantidade: int, data: datetime = None):
        self.id_produto = id_produto
        self.tipo = tipo
        self.quantidade = quantidade
        self.data = data if data else datetime.now()

# Algoritmos de Cadastro e Consulta
produtos = {}
categorias = {}
movimentacoes = []

# cadastrar categoria
def cad_categoria(nome: str):
    if nome not in categorias:
        categorias[nome] = Categoria(nome)
        print(f"\nCategoria '{nome}' cadastrada com sucesso!")
    else:
        print(f"\nCategoria '{nome}' já existe.")

# cadastrar produto
def cad_produto(id_produto: int, nome: str, nome_categoria: str, preco: float, quantidade: int):
    if id_produto <= 0:
        print("\nID inválido. Digite um número maior que 0.")
        return
    
    if id_produto in produtos:
        print(f"\nProduto com ID {id_produto} já existe.")
        return
    
    if nome_categoria not in categorias:
        print(f"\nCategoria '{nome_categoria}' já existe.")
        return
    
    produto = Produto(id_produto, nome, categorias[nome_categoria], preco, quantidade)
    produtos[id_produto] = produto
    print(f"\nProduto '{nome}' cadastrado com sucesso!")

# consulta de produto
def consultar_produto(id_produto: int):
    produto = produtos.get(id_produto)

    if produto:
        print(f"\nID: {produto.id_produto}, Nome: {produto.nome}, Categoria: {produto.categoria.nome}, Preço: {produto.preco}, Quantidade em estoque: {produto.quantidade}.")

    else:
        print(f"\nProduto com ID {id_produto} não encontrado.")

# movimentação de estoque (entrada e saída)
def movi_estoque(id_produto: int, tipo: str, quantidade: int):
    if id_produto not in produtos:
        print(f"\nproduto com ID {id_produto} não encontrado.")
        return
    
    if tipo not in ["entrada", "saida"]:
        print(f"\nTipo de movimentação inválido. Use 'entrada' ou 'saida'.")
        return

    produto = produtos[id_produto]    

    if tipo == "saida" and produto.quantidade < quantidade:
        print(f"\nEstoque insuficiente para realizar a saída de {quantidade} unidades.")
        return
    
    if tipo == "entrada":
        produto.quantidade += quantidade
    elif tipo == "saida":
        produto.quantidade -= quantidade

    movimentacao = Movimentacao(id_produto, tipo, quantidade)
    movimentacoes.append(movimentacao)
    print(f"\nMovimentação de tipo {tipo} de {quantidade} unidades do produto '{produto.nome}' foi registrada com sucesso.")

#  Relatórios e Consultas
def gerar_relato_produtos():
    print("\nRelatório de Produtos:")
    for produto in produtos.values():
        print(f"ID: {produto.id_produto}, Nome: {produto.nome}, Categoria: {produto.categoria.nome}, Preco: {produto.preco}, Quantidade em estoque: {produto.quantidade}")

def consultar_hist_movi(id_produto: int):
    produto = produtos[id_produto]

    print(f"\nHistórico de movimentações (ID = {id_produto}, Nome = {produto.nome}):")
    for movimento in movimentacoes:
        if movimento.id_produto == id_produto:
            print(f"Data: {movimento.data}, Tipo: {movimento.tipo}, Quantidade: {movimento.quantidade}")

# adicionando categorias
cad_categoria("Ferramenta")
cad_categoria("Material")
cad_categoria("Jardinagem")

# adicionando produtos
cad_produto(1, "Martelo", "Ferramenta", 15.50, 40)
cad_produto(2,"Rejunte", "Material", 30.00, 100)
cad_produto(3, "Cortador de grama", "Jardinagem", 400.00, 15)

# movimentando estoque
movi_estoque(1, "entrada", 10)
movi_estoque(1, "saida", 30)
movi_estoque(1, "entrada", 20)
movi_estoque(2, "saida", 46)
movi_estoque(3, "saida", 7)

# gerando relatório dos produtos
gerar_relato_produtos()

# consultando o histórico
consultar_hist_movi(1)
consultar_hist_movi(2)
consultar_hist_movi(3)