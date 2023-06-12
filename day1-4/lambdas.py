#!/usr/bin/env python3


def transforma_em_maiusculo(texto):
    return texto.upper()


def transforma_em_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


# e nossa funcao principal


def faz_algo(valor, funcao):
    print(f"Aplicando {funcao} em {valor}")
    return funcao(valor)

names = ["Alice", "Ana", "Sofia", "Soraya", "Helena", "Josélia", "Flávia", "Fernanda"]

print(sorted(names, key=lambda name: name.count("a")))
print(list(filter(lambda name: name[0].lower() == "f", names)))
print(list(map(lambda name: "Hello " + name, names)))

# Calculadora

operacao = input("operacao: [sum, mul, div, sub]:").strip()
n1 = input("n1:").strip()
n2 = input("n2:").strip()

operacoes = {
    "sum" : lambda a, b: a + b,
    "sub" : lambda a, b: a - b,
    "mul" : lambda a, b: a * b,
    "div" : lambda a, b: a / b,
}

resultado = operacoes[operacao](int(n1), int(n2))
print(f"O resultado é: {resultado}")