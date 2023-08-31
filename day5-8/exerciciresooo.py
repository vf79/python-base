from decimal import Decimal
import ipdb

class Produto:
    """Classe de produto"""

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = Decimal(valor)


maca = Produto("maçã", 4.5)
melancia = Produto("melancia", 6.3)

produtos = {
    "1": maca,
    "2": melancia
}

print("Olá cliente, boas vindas à quitanda!")
print("Estes são os produtos disponíveis:")
for codigo, produto in produtos.items():
    print(f"{codigo} -> {produto.nome} - R$ {produto.valor:.2f}")



class Compra:
    """Classe de compra de clientes"""
    def __init__(self, cliente_name, items=None):
        self.cliente_name = cliente_name
        self.items = items or []


    def add_item(self, produto, quantidade):
        produto.quantidade = quantidade
        self.items.append(produto)


    def calcula_total(self):
        total = 0
        # ipdb.set_trace()
        for produto in self.items:
            total += produto.valor * produto.quantidade
        return Decimal(total)


compra = Compra(cliente_name=input("Qual o seu nome? "))

while True:
    cod_produto = input("Código do produto: [enter para sair]").strip()
    if not cod_produto:
        break
    if cod_produto not in produtos:
        print("Codigo inválido tente novamente.")
        continue
    quantidade = int(input("Quantas Unidades?:").strip())
    compra.add_item(produtos[cod_produto], quantidade)

print(f"Olá, {compra.cliente_name}")
print(f"No seu carrinho de compras tem {len(compra.items)} itens.")
print(f"O total da compra é {compra.calcula_total():.2f}")