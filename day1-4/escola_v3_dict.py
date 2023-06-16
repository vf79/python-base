#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das
atividades.
"""
__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]


aulas = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala

for aula, alunos in aulas.items():
    print(f"Alunos da atividade {aula}\n")
    print("-" * 80)

    atividade_sala1 = []
    atividade_sala2 = []

    atividade_sala1 = set(sala1) & set(alunos)
    atividade_sala2 = set(sala2).intersection(alunos)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)
    print()
    print("-" * 80)

    # for aluno in alunos:
    #    if aluno in sala1:
    #        atividade_sala1.append(aluno)
    #    elif aluno in sala2:
    #        atividade_sala2.append(aluno)
#
# print("Sala1 ", atividade_sala1)
# print("Sala2 ", atividade_sala2)
# print()
# print("-" * 80)
#
