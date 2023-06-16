#!/bin/usr/env python3
"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""

# SOLID -> S - Single responsibility


def f(x):  # assinatura
    result = 5 * (x / 2)
    return result


def double(x):
    return x * 2


valor = double(f(10))

print(f(10))
print(valor)


###
def print_in_upper(text):
    """Procedure with no explicit return"""
    print(text.upper())
    # implicit return None


print_in_upper("maiusculo")


###
def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    return area


def heron2(params):
    return heron(*params)


triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
]

# print(list(map(heron2, triangulos))) Exemplo de map

for t in triangulos:
    area = heron(*t)  # Desempacotando na chamada da função
    print(f"A area do triangulo é: {area}")
    area = heron2(t)
    print(f"A area do triangulo é: {area}")  # Desempacotando dentro da função.

###


def nome_da_funcao():
    print("Hello funcão")
    return 1


result = nome_da_funcao()
print(result)
