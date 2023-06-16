#!/bin/usr/env python3

# aqui começa o escopo global
nome = "Global"


def funcao():
    # aqui começa o escopo local da funcao
    nome = "Local"

    def funcao_interna():  # inner function
        # aqui começa o escopo local da funcao interna
        nome = "Interna"

        # print("Escopo local da funcao interna:", locals())
        # print("*" * 80)
        print(nome)
        return nome
        # aqui termina o escopo local da funcao interna

    # print("Escopo local da função: ",locals())
    # print("=" * 80)
    funcao_interna()
    print(nome)
    return nome
    # aqui termina o escopo local da funcao


# print("Escopo global do programa: ", globals())
# print("-" * 80)
funcao()
print(nome)
# print("-" * 80)
# aqui termina o escopo global
